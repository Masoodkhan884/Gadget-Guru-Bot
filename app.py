import streamlit as st

from src.retriever import retrieve_context
from src.llm import generate_answer

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Gadget Guru Bot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🤖 Gadget Guru Bot")
st.caption("AI Customer Support for AeroPress Pro 5 Coffee Maker")

# -----------------------------
# SESSION STATE (CHAT MEMORY)
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.chat_input("Ask something about AeroPress Pro 5...")

# -----------------------------
# MAIN LOGIC
# -----------------------------
if user_input:

    # Step 1: Retrieve context from Pinecone
    context = retrieve_context(user_input)

    # Step 2: Generate answer using Groq LLM
    answer = generate_answer(user_input, context)

    # Step 3: Save chat history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", answer))

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for role, message in st.session_state.chat_history:

    if role == "user":
        st.markdown(f"🧑‍💻 **You:** {message}")

    else:
        st.markdown(f"🤖 **Bot:** {message}")
        st.markdown("---")