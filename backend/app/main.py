from fastapi import FastAPI
from pydantic import BaseModel

from app.agents.travel_agents import travel
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TravelRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI Travel Agent is running"
    }


@app.post("/plan-trip")
def plan_trip(request: TravelRequest):

    result = travel.invoke({
        "messages": [
            {
                "role": "user",
                "content": request.message
            }
        ]
    })

    final_message = result["messages"][-1].content

    return {
        "response": final_message
    }