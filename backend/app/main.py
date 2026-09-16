import os
import json

from fastapi import FastAPI
from dotenv import load_dotenv
from groq import Groq

from app.tools.weather import get_weather


load_dotenv()

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.get("/")
def home():
    return {
        "message": "AI Travel Agent is running"
    }


@app.post("/plan-trip")
def plan_trip(message: str):
    messages = [
        {
            "role": "system",
            "content": ("You are an AI travel assistant. Use the weather tool whenever the user asks about weather."
            )
        },
        {
            "role": "user","content": message
        }
    ]

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

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    assistant_response = response.choices[0].message

    if assistant_response.tool_calls:
        for tool_call in assistant_response.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(
                tool_call.function.arguments
            )

            if function_name == "get_weather":

                tool_result = get_weather(
                    arguments["city"]
                )
            else:
                tool_result = {
                    "error": "Unknown tool"
                }
            final_messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an AI travel assistant.Answer the user using the tool result."
                    )
                },
                {
                    "role": "user","content": message
                },
                {
                    "role": "user",
                    "content": (
                        "The weather tool returned this result: "
                        + json.dumps(tool_result)
                    )
                }
            ]

            final_response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=final_messages
            )
            return {
                "response": final_response.choices[0].message.content
            }
    return {
        "response": assistant_response.content
    }