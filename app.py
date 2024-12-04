## first download the model llama-2-7b-chat-ggml from huggingface and then store it locally
## then create a conda venv using conda create -p venv python==3.9 and then activate it
## then install thee libraries sentence-transformers,uvicorn,ctransformers,langchain,python-box,streamlit 
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getllamaresponse(input_text,no_words,blog_style):
    llm=CTransformers(model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01,
                              })
    tempelate="""
                Write a blog for {blog_style} job profile for the top {input_text} within {no_words}.
            """
    prompt=PromptTemplate(input_variables=['blog_style','no_words','blog_style'],
                          template=tempelate)
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs🤖")
input_text=st.text_input("Enter the Blog topic")

## Create two more additional fields
col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input("No. of words")
with col2:
    whowrite=st.selectbox("Writing the blog for",("Researchers","Students","Data Scientists"),index=0)

submit=st.button("Generate")

if submit:
    st.write(getllamaresponse(input_text,no_words,whowrite))