from typing import TypedDict
from langgraph.graph import StateGraph,START,END
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage
import os
from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode , tools_condition
from app.tools.weather import get_weather
from app.tools.places import get_places
import json
from groq import Groq
load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))
tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather for a given city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "Name of the city"
                        }
                    },
                    "required": ["city"]
                }
            }
        }
    ]




class TravelState(MessagesState):
    pass

def llm_node(state:TravelState):
    user_message=state["messages"][-1].content
    response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages= [
        {
            "role": "system",
            "content": ("You are an AI travel assistant. Use the weather tool whenever the user asks about weather."
            )
        },
        {
            "role": "user","content": user_message
        }
    ],
    tools=tools,
    tool_choice="auto"
    )

    assistant_message=response.choices[0].message
    print("Content:",assistant_message.content)
    print("Tool calls:",assistant_message.tool_calls)
    tool_calls=[]
    if assistant_message.tool_calls:
        for tool_call in assistant_message.tool_calls:
            tool_calls.append({
                "name":tool_call.function.name,
                "args":json.loads(tool_call.function.arguments),
                "id":tool_call.id
            })
    return {
        "messages": [AIMessage(content=assistant_message.content or "",tool_calls=tool_calls)]
    }

    
tool_node=ToolNode([get_weather,get_places])
graph_builder=StateGraph(TravelState)

graph_builder.add_node("llm",llm_node)
graph_builder.add_node("tools",tool_node)

graph_builder.add_edge(START,"llm")
graph_builder.add_conditional_edges("llm",tools_condition)
graph_builder.add_edge("tools","llm")
graph_builder.add_edge("llm",END)

travel=graph_builder.compile()
result=travel.invoke({"messages": [{"role": "user", "content": "Weather in Goa"}]})
print(result)
