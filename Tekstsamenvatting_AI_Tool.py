import streamlit as st
from chatbot_functies import chatbot_response


st.title("🤖 Learning AI 🤖")
st.markdown("Tekstsamenvatting Tool")
form = st.form(key="user_settings")
with form:
    full_text = st.text_area("Geef hier de tekst in die je wil samenvatten:",height=500, key = "full_text")
    generate_button = form.form_submit_button("Creëer samenvatting")
    if generate_button:
        with st.spinner('Wait for it...'): #add a waiting icon while waiting for the response
            PROMPT = f"Concisely summarize the text {full_text} within' a limited amount of sentences."
            response = chatbot_response(PROMPT)
        st.write(response)
