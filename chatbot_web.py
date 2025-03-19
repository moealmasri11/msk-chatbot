import streamlit as st
import openai

# Set up the OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

# Streamlit UI
st.title("AI-Powered MSK Physiotherapy Chatbot 💬")
st.write("Describe your symptoms, and the chatbot will provide rehabilitation advice.")

# User input
user_input = st.text_input("Enter your symptoms here:")

# Chatbot response
if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert physiotherapist. Ask follow-up questions if needed before providing rehab advice."},
            {"role": "user", "content": user_input}
        ]
    )
    st.subheader("Chatbot Response:")
    st.write(response["choices"][0]["message"]["content"])
