from langchain_chroma import Chroma
from app.rag.embeddings import get_embeddings

CHROMA_PATH = "app/chroma_db"


def create_db(chunks):

    embeddings = get_embeddings()

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    # Print metadata (temporary)
    if not chunks:
        print("No chunks found!")
        return

    
    print(chunks[0].metadata)

    db.add_documents(chunks)

    return db


def load_db():

    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embeddings()
    )