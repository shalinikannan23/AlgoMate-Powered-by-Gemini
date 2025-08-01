# AlgoMate – Domain-Specific Coding AI Agent Powered by Gemini

## Abstract
AlgoMate is an **AI-powered programming assistant** built using **LangGraph and Google Gemini API** that focuses exclusively on solving coding problems, debugging programs, and mentoring developers.  
Unlike general-purpose chatbots, AlgoMate is **domain-specific**: it acts as an **AI Agent** capable of reasoning over programming queries, analyzing user-provided code, generating optimized solutions, and providing explanations step by step.

### Key Features
- Uses **Gemini 1.5 Flash** for high-quality reasoning
- Designed as a **multi-turn AI Agent** with memory for coding tasks
- Streamlit-based chat UI with a **modern, coding-themed interface**
- Personalized support for algorithms, debugging, and learning coding concepts

---

## Program
The solution is implemented in **Python** with the following stack:

- **LangGraph** – to build the agent workflow (reasoning + tool calls)
- **Streamlit** – for an interactive chat interface
- **LangChain Google GenAI** – to integrate Gemini models
- **StateGraph Agent** – custom logic for AI agent actions and responses

**Core Files:**
- `agent_class.py` – Defines the Agent logic and workflow
- `app.py` – Streamlit UI to interact with the agent
- `.env` – Stores your Google API key securely

**Output:**

<img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/deacdebc-d47f-4157-b102-27621aca0284" />

<img width="1919" height="970" alt="image" src="https://github.com/user-attachments/assets/b06b512e-80bf-4d39-a12b-4cc72b9f7a40" />

<img width="1919" height="971" alt="image" src="https://github.com/user-attachments/assets/670efc5f-6b1a-4f75-b74a-8c4c18598ac2" />

## Result
AlgoMate successfully works as a **domain-specific coding AI assistant**.  
It can:
- Understand programming questions
- Generate optimized, well-explained solutions
- Debug and improve user-provided code
- Provide step-by-step reasoning for algorithms

This project demonstrates how **LangGraph + Gemini** can be combined to create a specialized AI Agent with an interactive chat interface.

**Outcome:**  
A working Streamlit-based coding mentor that answers programming queries accurately in real time.
