from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain

from langchain_ollama import ChatOllama

from app.rag.vectorstore import load_db


def get_document_chain(document: str):

    db = load_db()

    retriever = db.as_retriever(
        search_kwargs={
            "k": 20,
            "filter": {
                "source": f"app/uploads/{document}"
            }
        }
    )

    llm = ChatOllama(
        model="llama3.2",
        base_url="http://host.docker.internal:11434",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful AI assistant.

Answer ONLY from the provided context.

If the answer is not available,
reply:

I don't know based on the uploaded document.

Context:
{context}

Question:
{input}
"""
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    return create_retrieval_chain(
        retriever,
        document_chain
    )