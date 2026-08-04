from app.rag.loaders import load_pdf
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore


PDF_PATH = "app/uploads/company_policy.pdf"


def ingest():

    print("Loading PDF...")

    documents = load_pdf(PDF_PATH)

    print(f"Pages Loaded : {len(documents)}")

    print("Splitting...")

    chunks = split_documents(documents)

    print(f"Chunks Created : {len(chunks)}")

    print("Creating Vector Database...")

    create_vectorstore(chunks)

    print("Done!")


if __name__ == "__main__":
    ingest()