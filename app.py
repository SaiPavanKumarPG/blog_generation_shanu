import streamlit as st
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# function to get response from model llms3

template = """
Write a blog for {blog_style} on the topic "{input_text}" within {no_words} words.
"""
model = OllamaLLM(model = 'llama3')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model



def getLlamaResponse(input_text, no_words, blog_style):
    response = chain.invoke({"input_text": input_text, "no_words": no_words, "blog_style": blog_style})
    print(response)
    return response




st.set_page_config(page_title="Generate Blogs",
                   page_icon="📝",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.title("Generate Blogs")

input_text = st.text_input("Enter the blog Topic")

## Creating to more columns for additional 2 fields
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words")
with col2:
    blog_style = st.selectbox("Select Blog Style", ["RESEARCH", "DATA SCIENTIST","COMMON PEOPLE"])

submit = st.button("Generate Blog")

# Final response
if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))
