'''

OPENAI_API_KEY = "sk-HuasupkDPWCkesrUKvrRT3BlbkFJVFFrleMKuoEMGvy2cn2"
LANGCHAIN_API_KEY="djfhshkshfskhfjdfhfjfhjhfdjhfhj"
LANGCHAIN_PROJECT="Project1"
'''

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os 
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
#langchain smith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistent.Please Response to the user queries"),
            ('user', 'Question:{question}')
        ]
    )


llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
)

#streamlit framwork
st.title('Langchain Demo with OpenAI APi')

input_text=st.text_input("Search the topic you want")

parser = StrOutputParser()

chain = prompt | llm | parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

