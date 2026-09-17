import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import SystemMessage


from app.tools.weather import get_weather
from app.tools.places import get_places
from app.tools.flights import get_flights
from app.tools.hotels import get_hotels


load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


llm_with_tools = llm.bind_tools([
    get_weather,
    get_places,
    get_flights,
    get_hotels
])

SYSTEM_PROMPT = """
You are a reliable AI travel assistant.

Rules:
1. Use tool results as the primary source of factual information.
2. Never invent flight prices, hotel prices, visa rules, baggage allowances,
   flight durations, airline details, or weather information.
3. If a requested detail is not available from the tools, clearly say:
   "I don't have verified information for this detail."
4. Do not add random tourist places that were not returned by the places tool.
5. Clearly distinguish between live tool data and general travel suggestions.
6. Give concise, structured and useful answers.
"""



class TravelState(MessagesState):
    pass



def llm_node(state: TravelState):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"]
    ]

    response = llm_with_tools.invoke(messages)

    print("Content:", response.content)
    print("Tool calls:", response.tool_calls)

    return {
        "messages": [response]
    }

tool_node = ToolNode([
    get_weather,
    get_places,
    get_flights,
    get_hotels
])


graph_builder = StateGraph(TravelState)

graph_builder.add_node("llm", llm_node)
graph_builder.add_node("tools", tool_node)

# START → LLM
graph_builder.add_edge(
    START,
    "llm"
)


graph_builder.add_conditional_edges(
    "llm",tools_condition
)


graph_builder.add_edge(
    "tools","llm"
)

travel = graph_builder.compile()



