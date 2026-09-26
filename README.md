<div align="center">

# ✈️ AI Travel Agent

### 🌍 Intelligent AI-Powered Travel Planning Assistant

An AI travel agent that understands natural-language travel queries and uses real-world APIs to provide weather, tourist places, flights and hotel information.

**React • FastAPI • LangGraph • Groq • Real-World APIs**

</div>

---

## 🌟 Features

- 🤖 AI-powered travel assistant
- 🧠 LangGraph-based AI agent
- 🔧 Automatic tool calling
- 🌤️ Real-time weather information
- 📍 Tourist places search
- ✈️ Flight information
- 🏨 Hotel search
- ⚡ FastAPI backend
- 💻 React frontend
- 🔄 Multi-tool travel queries
- 🔐 Environment-based API key management

---

## 🏗️ Architecture

    User
      ↓
    React Frontend
      ↓
    FastAPI Backend
      ↓
    LangGraph AI Agent
      ↓
    Groq LLM
      ↓
    ┌──────────┬──────────┬──────────┬──────────┐
    ↓          ↓          ↓          ↓
    Weather   Places     Flights    Hotels
    ↓          ↓          ↓          ↓
    Open-      Geoapify  Aviation-  SerpApi
    Meteo                 stack
    ↓          ↓          ↓          ↓
    └──────────┴──────────┴──────────┘
                    ↓
              Tool Results
                    ↓
                 Groq LLM
                    ↓
              Final Response
                    ↓
             React Frontend

---

## 🧠 How the AI Agent Works

This project is an AI agent rather than a simple chatbot.

The user sends a natural-language travel query. The Groq LLM understands the query and decides which tool or tools are required.

    User Query
        ↓
    Groq LLM
        ↓
    Tool Required?
       / \
     Yes  No
      ↓    ↓
    Tool   Final Answer
      ↓
    External API
      ↓
    Tool Result
      ↓
    Groq LLM
      ↓
    Final Answer

### Example

User asks:

    "What is the weather in Delhi?"

The agent performs:

    User
      ↓
    Groq LLM
      ↓
    get_weather("Delhi")
      ↓
    Open-Meteo API
      ↓
    Weather Result
      ↓
    Groq LLM
      ↓
    Final Response

For a multi-tool query:

    "Plan a trip from Delhi to Goa.
     Tell me the weather, places, flights and hotels."

The agent can call:

    Weather Tool
    Places Tool
    Flights Tool
    Hotels Tool

The results are then passed back to the LLM to generate the final response.

---

## 🔄 LangGraph Workflow

LangGraph manages the agent workflow using state, nodes and conditional edges.

    START
      ↓
    LLM Node
      ↓
    Tool Required?
      │
      ├── No ─────────→ END
      │
      └── Yes
           ↓
        Tool Node
           ↓
        Tool Result
           ↓
        LLM Node
           ↓
      Tool Required?
           │
           ├── Yes → Tool Node
           │
           └── No  → END

### Main LangGraph Components

**State**

Stores the current conversation and messages.

**LLM Node**

Sends the conversation to the Groq LLM.

**Tool Node**

Executes the tool requested by the LLM.

**Conditional Edge**

Checks whether the LLM requested a tool.

**Messages**

Maintain the conversation and tool results throughout the workflow.

---

## 🛠️ Tools

### 🌤️ Weather Tool

Uses Open-Meteo to retrieve current weather information.

Provides:

- Temperature
- Humidity
- Wind speed
- Weather code
- Location

### 📍 Places Tool

Uses Geoapify to search for tourist attractions and places in a city.

### ✈️ Flights Tool

Uses Aviationstack to retrieve flight information between airports.

Provides:

- Airline
- Flight number
- Flight status
- Departure airport
- Arrival airport
- Scheduled departure
- Scheduled arrival

### 🏨 Hotels Tool

Uses SerpApi Google Hotels search to retrieve hotel information.

Provides:

- Hotel name
- Rating
- Reviews
- Price
- Amenities
- Hotel link

---

## 🛠️ Technology Stack

### Frontend

- React
- Vite
- Tailwind CSS
- JavaScript
- Fetch API

### Backend

- Python
- FastAPI
- LangChain
- LangGraph

### LLM

- Groq
- GPT-OSS-120B

### External APIs

| Purpose | API |
|---|---|
| 🌤️ Weather | Open-Meteo |
| 📍 Places | Geoapify |
| ✈️ Flights | Aviationstack |
| 🏨 Hotels | SerpApi |

---

## 📁 Project Structure

    Travel_Agent/
    │
    ├── backend/
    │   │
    │   ├── app/
    │   │   │
    │   │   ├── agents/
    │   │   │   └── travel_agents.py
    │   │   │
    │   │   ├── tools/
    │   │   │   ├── weather.py
    │   │   │   ├── places.py
    │   │   │   ├── flights.py
    │   │   │   └── hotels.py
    │   │   │
    │   │   └── main.py
    │   │
    │   ├── .env
    │   └── requirements.txt
    │
    ├── frontend/
    │   │
    │   ├── public/
    │   ├── src/
    │   ├── package.json
    │   └── vite.config.js
    │
    └── README.md

---

## 📄 Important Files

### `backend/app/main.py`

FastAPI entry point.

Responsibilities:

- Creates the FastAPI application
- Defines API endpoints
- Receives travel queries
- Sends queries to the LangGraph agent
- Returns the final AI response

### `backend/app/agents/travel_agents.py`

Contains the main AI agent.

Responsibilities:

- Creates the Groq LLM
- Connects tools to the LLM
- Defines the travel state
- Creates LangGraph nodes
- Controls the agent workflow
- Handles tool-calling loops

### `backend/app/tools/weather.py`

Contains the weather tool and Open-Meteo integration.

### `backend/app/tools/places.py`

Contains the places tool and Geoapify integration.

### `backend/app/tools/flights.py`

Contains the flights tool and Aviationstack integration.

### `backend/app/tools/hotels.py`

Contains the hotels tool and SerpApi integration.

---

## 🔌 API

### Endpoint

    POST /plan-trip

### Request

    {
      "message": "Plan a trip from Delhi to Goa"
    }

### Response

    {
      "response": "Here is your travel information..."
    }

---

## 💬 Example Queries

    What is the weather in Delhi?

    What are the tourist places in Goa?

    Show flights from Delhi to Mumbai.

    Find hotels in Goa.

    Plan a trip from Delhi to Goa for 2 people.

    Tell me the weather, places, flights and hotels for Goa.

---

## 🚀 Installation

### 1. Clone the Repository

    git clone <your-repository-url>
    cd Travel_Agent

### 2. Setup Backend

    cd backend
    python -m venv venv

Windows:

    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

### 3. Create Environment Variables

Create:

    backend/.env

Add:

    GROQ_API_KEY=your_groq_api_key
    GEOAPIFY_API_KEY=your_geoapify_api_key
    AVIATION_API_KEY=your_aviation_api_key
    SERPAPI_API_KEY=your_serpapi_api_key

### 4. Start Backend

    uvicorn app.main:app --reload

Backend:

    http://127.0.0.1:8000

Swagger:

    http://127.0.0.1:8000/docs

### 5. Start Frontend

Open another terminal:

    cd frontend
    npm install
    npm run dev

---

## 🔐 Security

API keys are stored in `.env` and should never be committed to GitHub.

Recommended `.gitignore`:

    .env
    .env.local
    node_modules/
    dist/
    __pycache__/
    *.pyc

---

## 📊 Current Status

| Component | Status |
|---|---|
| FastAPI Backend | ✅ |
| Groq LLM | ✅ |
| LangGraph Agent | ✅ |
| Tool Calling | ✅ |
| Weather Tool | ✅ |
| Places Tool | ✅ |
| Flights Tool | ✅ |
| Hotels Tool | ✅ |
| React Frontend | ✅ |
| Frontend ↔ Backend | ✅ |
| Multi-tool Queries | ✅ |

---

## 🔮 Future Improvements

- 🗺️ Interactive maps
- 📅 Advanced itinerary generation
- 💰 Budget estimation
- 💬 Conversation memory
- 🌐 Cloud deployment
- 📱 Improved mobile experience
- 🧭 Additional travel tools

---

## ⚠️ Disclaimer

This application uses external APIs and AI-generated responses to provide travel information. Flight schedules, hotel availability, prices and other travel details may change. Important travel and booking information should be independently verified before making final arrangements.

---

<div align="center">

## ✈️ Plan Smarter. Travel Better. 🌍

Built with ❤️ using

**React • FastAPI • LangGraph • Groq**

### 👩‍💻 Anushka Singh

**B.Tech — Artificial Intelligence & Data Science**

</div>