# Finance Chatbot 💸

A simple finance-focused chatbot built with **Streamlit** and **Groq/LLM integration**.  
It allows users to ask questions about finances, view responses, and track their chat history in a sidebar.

---

## 🚀 Features
- Interactive finance Q&A powered by LLM (`get_chat_response`).
- Persistent **chat history** stored in `st.session_state`.
- Sidebar view of past queries for quick reference.
- Clean Streamlit UI with finance-themed icons.

---

## 📂 Project Structure

finance-chatbot/
│
├── app.py                # Main Streamlit app
├── llm.py                # Contains get_chat_response and build_messages
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

RUN:streamlit run app.py


Usage
Type your finance-related query in the input box.

Click Ask to get a response.

View your conversation history in the sidebar.

Scroll down to see the full conversation log.