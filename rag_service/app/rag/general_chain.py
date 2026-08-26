from langchain_groq import ChatGroq

llm = ChatGroq(

    model="openai/gpt-oss-120b",

    temperature=0.3

)


def get_general_chain():

    return llm