from langchain_groq import ChatGroq

llm = ChatGroq(

    model="llama-3.3-70b-versatile",

    temperature=0.3

)


def get_general_chain():

    return llm