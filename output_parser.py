from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
)


def call_string_output_parser():

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Tell me a joke about a {input}"),
            ('human', 'input')
        ]
    )


    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain.invoke({"input": "cat"})

# print(call_string_output_parser())
def call_list_output_parser():

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Generate alist of 10 sysnonyms  for the following words. Return the result in omma seprated list."),
            ('human', 'input')
        ]
    )


    parser = CommaSeparatedListOutputParser()

    chain = prompt | llm | parser

    return chain.invoke({"input": "happy"})


# print(call_list_output_parser())
# print(type(call_list_output_parser()))

#JSON OUTPUT PARSER EXAMPLE
def call_json_output_parser():

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract information from the following phrase.\nFormatting Instructions: {format_instructions}"),
        ("human", "{phrase}")
    ])

    class Person(BaseModel):
        recipe: str= Field(description='the name of the recipe')
        ingrediets: list= Field(description='ingrediets')



    parser = JsonOutputParser(pydantic_object=Person)

    chain = prompt | llm | parser

    return chain.invoke({
        "phrase": "The ingrediet for a Margghrita pizza are tomatos, onions,cheese, basil",
        "format_instructions": parser.get_format_instructions()
        })

print(type(call_json_output_parser()))
print(call_json_output_parser())