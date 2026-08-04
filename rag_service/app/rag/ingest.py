from app.rag.loaders import load_pdf
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_db


def ingest(pdf_path: str):

    print("Loading PDF...")

    docs = load_pdf(pdf_path)

    print("Pages:", len(docs))

    print("Splitting...")

    chunks = split_documents(docs)

    print("Chunks:", len(chunks))

    print("Creating Vector DB...")

    create_db(chunks)

    print("Done!")