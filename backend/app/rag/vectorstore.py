from langchain_chroma import Chroma

from app.rag.embeddings import get_embeddings


CHROMA_PATH = "app/rag/chroma_db"


def create_vectorstore(chunks):

    embeddings = get_embeddings()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    return db


def load_vectorstore():

    embeddings = get_embeddings()

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    return db