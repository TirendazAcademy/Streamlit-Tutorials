from dotenv import load_dotenv 
import anthropic
import streamlit as st

load_dotenv()

def get_response(user_content): 
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system="Generate 5 attention-grabbing blog titles based on user-provived keywords",
        messages=[{"role":"user", "content":user_content}],
    )
    return response.content[0].text

st.title("Blog Title Generator")
user_content = st.text_input("Enter the keyword for blog titles:")

if st.button("Generate Titles"):
    if not user_content:
        st.warning("Please enter a keyword before generating titles.", icon = "⚠️")
    generated_titles = get_response(user_content)
    st.success("Titles generated successfully!")
    st.text_area("", value=generated_titles, height=300)





