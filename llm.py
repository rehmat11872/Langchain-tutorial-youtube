from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
)

# response = llm.invoke("How are you")

# response = llm.batch(['how are you', 'What is AI?'])

response = llm.stream("How are you")



for chunk in response:
    print(chunk.content, end="", flush=True)


