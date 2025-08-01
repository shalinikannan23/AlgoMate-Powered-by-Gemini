import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from agent_class import Agent
import streamlit as st

load_dotenv()

# Custom CSS for chat layout
custom_css = """
<style>
.chat-wrapper {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.user-bubble, .bot-bubble {
    padding: 12px 16px;
    border-radius: 15px;
    margin: 8px 0;
    max-width: 80%;
    font-size: 16px;
    line-height: 1.5;
    word-wrap: break-word;
}

.user-bubble {
    background: #00C2FF;
    color: black;
    margin-left: auto;
}

.bot-bubble {
    background: #252831;
    color: white;
    margin-right: auto;
    border: 1px solid #3A3F4B;
}

input[type="text"] {
    font-size: 18px !important;
}

.stButton>button {
    background-color: #00C2FF;
    color: black;
    border: none;
    padding: 8px 20px;
    font-size: 16px;
    border-radius: 10px;
}
</style>
"""

# ... same imports ...

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:#00C2FF;'>CodeSphere - Programming Assistant</h1>", unsafe_allow_html=True)

# Chat container
st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask coding questions or debugging help:")

# Initialize programming-specific agent
if "abot" not in st.session_state:
    # Programming-focused system prompt
    prompt = """
    You are CodeSphere, a highly skilled coding assistant.
    - Specialize in Python, JavaScript, Java, C++, and modern frameworks.
    - Help with debugging, algorithms, explaining concepts, writing code.
    - When providing code, always give clean, optimized, and well-commented examples.
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    st.session_state.abot = Agent(model, [], system=prompt)

# On send
if st.button("Send") and query.strip():
    st.session_state.history.append(("user", query))
    messages = [HumanMessage(content=query)]
    result = st.session_state.abot.graph.invoke({"messages": messages})
    response = result['messages'][-1].content
    st.session_state.history.append(("bot", response))

# Show chat bubbles
for role, text in st.session_state.history:
    if role == "user":
        st.markdown(f'<div class="user-bubble">{text}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{text}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
