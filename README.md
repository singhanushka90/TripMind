<div align="center">

# ✈️ AI Travel Agent

### Your Intelligent AI-Powered Travel Planning Assistant 🌍

Plan trips, explore destinations, check weather, discover hotels,
and search flights through a single AI-powered travel assistant.

<br>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-FF6B35?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge)
![Vite](https://img.shields.io/badge/Vite-Frontend-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

<br>

**An AI agent that combines LLM reasoning with real-world travel APIs.**

</div>

---

# 🌍 About The Project

**AI Travel Agent** is a full-stack AI-powered travel planning
application that allows users to ask travel-related questions using
natural language.

Instead of manually searching multiple travel websites for weather,
tourist attractions, hotels and flights, the AI agent can decide
which tools are required, retrieve information from external APIs,
and combine the results into a useful response.

### Example Query

> Plan a 3-day trip from Delhi to Goa for 2 people. Tell me about the
> weather, hotels, places to visit and flights.

The AI agent analyzes the request and can use multiple tools to
collect the required travel information.

---

# ✨ Features

| Feature | Description |
|---|---|
| 🤖 AI Travel Assistant | Understands natural-language travel queries |
| 🧠 AI Agent | Uses LangGraph for agent orchestration |
| 🌤️ Weather | Retrieves weather information using Open-Meteo |
| 📍 Tourist Places | Finds attractions using Geoapify |
| ✈️ Flight Search | Retrieves flight information using Aviationstack |
| 🏨 Hotel Search | Searches hotel information using SerpApi |
| 🔄 Multi-Tool Calling | Automatically selects the required tools |
| ⚡ FastAPI Backend | Provides the REST API |
| 💻 React Frontend | Single-page travel assistant interface |
| 📱 Responsive UI | Works across desktop and mobile |

---

# 🏗️ System Architecture

```text
                         👤 USER
                           │
                           ▼
                ┌─────────────────────┐
                │    React Frontend   │
                │   Vite + Tailwind   │
                └──────────┬──────────┘
                           │
                           │ HTTP POST
                           ▼
                ┌─────────────────────┐
                │       FastAPI       │
                │      /plan-trip     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      LangGraph      │
                │      AI Agent       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       Groq LLM      │
                │   GPT-OSS-120B      │
                └──────────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     🌤️ Weather       📍 Places        ✈️ Flights
     Open-Meteo       Geoapify        Aviationstack
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                       🏨 Hotels
                         SerpApi
                           │
                           ▼
                ┌─────────────────────┐
                │    Tool Results     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       Groq LLM      │
                │   Final Response    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    React Frontend   │
                └─────────────────────┘

🧠 How The AI Agent Works
The core of the application is an AI agent built using LangGraph.
The agent does not blindly call every API for every query.
Instead, the LLM analyzes the user's request and decides which tool or tools are relevant.


Agent Workflow

User Query
    │
    ▼
┌─────────────────┐
│     Groq LLM    │
│ Understand Query│
└────────┬────────┘
         │
         ▼
   Tool Required?
      /       \
    YES        NO
     │          │
     ▼          ▼
 ToolNode    Final Answer
     │
     ▼
External API
     │
     ▼
Tool Result
     │
     ▼
Groq LLM
     │
     ▼
Final Answer

Multi-Tool Example
For a query like:
Tell me the weather, hotels, tourist places and flights for my Delhi to Goa trip.

The agent can perform:

USER
                      │
                      ▼
                  GROQ LLM
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ▼              ▼              ▼
   Weather          Places         Flights
       │              │              │
 Open-Meteo        Geoapify      Aviationstack
       │              │              │
       └──────────────┼──────────────┘
                      │
                      ▼
                    Hotels
                      │
                    SerpApi
                      │
                      ▼
                 Tool Results
                      │
                      ▼
                  GROQ LLM
                      │
                      ▼
                FINAL RESPONSE

Tool Calling Concept
The LLM does not directly execute Python functions or external APIs.

The process is:

LLM
 ↓
Decides a tool is needed
 ↓
Tool Call
 ↓
Python Tool
 ↓
External API
 ↓
Tool Result
 ↓
LLM
 ↓
Final Response

🛠️ Technology Stack
Frontend
React
Vite
Tailwind CSS
JavaScript
Fetch API
Backend
Python
FastAPI
LangGraph
LangChain
Groq
External APIs
Service
Purpose
Open-Meteo
Weather data
Geoapify
Tourist places and attractions
Aviationstack
Flight information
SerpApi
Hotel search


📁 Project Structure

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
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── vite.config.js
│   └── .gitignore
│
└── README.md