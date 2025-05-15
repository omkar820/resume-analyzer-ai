
import streamlit as st
import openai

api_key = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=api_key)
import openai

client = openai.OpenAI(api_key=api_key)

def generate_feedback_with_gpt(resume_text):
    prompt = f"""
    You are an expert ATS system and HR. Review the following resume text and give:

    1. ATS Score (out of 100)
    2. Feedback on formatting, keywords, readability
    3. Suggestions to improve it
    4. Highlight missing keywords for a Data Scientist role

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=800
    )

    return response.choices[0].message.content
