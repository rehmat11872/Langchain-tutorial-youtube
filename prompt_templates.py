from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
)

# prompt = ChatPromptTemplate.from_template('Tell me a joke about a {input}')


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Genearte a list of 10 synonyms fron the following word"),
        ('human', 'input')
    ]
)

chain = prompt | llm

response = chain.invoke({"input": "sad"})

print(response)