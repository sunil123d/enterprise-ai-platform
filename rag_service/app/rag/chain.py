from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_classic.chains.retrieval import (
    create_retrieval_chain,
)

from langchain_groq import ChatGroq

from app.rag.hybrid_retriever import get_hybrid_retriever


def get_chain(selected_documents: list[str] = []):

    # -------------------------
    # Hybrid Retriever
    # -------------------------

    retriever = get_hybrid_retriever(
        selected_documents
    )

    # -------------------------
    # Groq LLM
    # -------------------------

    llm = ChatGroq(

        model="openai/gpt-oss-120b",

        temperature=0

    )

    # -------------------------
    # Prompt
    # -------------------------

    prompt = ChatPromptTemplate.from_template(
        """
You are Enterprise AI Assistant.

Use ONLY the provided context.

Always use the previous conversation when answering follow-up questions.

If the answer is not present inside the context say:

"I don't know based on the uploaded documents."

Conversation History:
{history}

Context:
{context}

Question:
{input}
"""
    )

    # -------------------------
    # Document Chain
    # -------------------------

    document_chain = create_stuff_documents_chain(

        llm,

        prompt

    )

    # -------------------------
    # Retrieval Chain
    # -------------------------

    retrieval_chain = create_retrieval_chain(

        retriever,

        document_chain

    )

    return retrieval_chain