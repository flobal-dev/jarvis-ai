import streamlit as st
from rag import build_index, query

st.set_page_config(page_title="Jarvis AI", page_icon="🧠")

st.title("🧠 Jarvis AI")
st.markdown("Frage deine Dokumente lokal (RAG + Mistral)")

# ✅ System laden (wichtig für Speed)
@st.cache_resource
def load_system():
    return build_index()

# Lade Index + LLM
with st.spinner("System wird geladen... ⏳"):
    index, llm = load_system()

st.success("✅ Jarvis ist bereit")

# Eingabe
user_input = st.text_input("Deine Frage:")

# Button
if st.button("Fragen") and user_input:

    with st.spinner("Jarvis denkt nach... 🤔"):
        response = query(index, llm, user_input)

    # ✅ CLEAN OUTPUT
    st.markdown("### 🤖 Antwort")
    st.markdown(response.response)

