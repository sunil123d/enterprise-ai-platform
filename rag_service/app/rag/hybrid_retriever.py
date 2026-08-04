import os

from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever
from langchain_core.documents import Document

from app.rag.vectorstore import load_db


def get_hybrid_retriever(selected_documents: list[str] = []):

    # Load ChromaDB
    db = load_db()

    # Load all documents from ChromaDB
    docs = db.get()

    all_documents = []

    for i in range(len(docs["documents"])):
        all_documents.append(
            Document(
                page_content=docs["documents"][i],
                metadata=docs["metadatas"][i]
            )
        )

    print("\n========== DOCUMENT METADATA ==========")
    for doc in all_documents:
        print(doc.metadata)
    print("=======================================\n")

    # -----------------------------
    # Vector Retriever
    # -----------------------------
    search_kwargs = {
        "k": 20
    }

    if selected_documents:
        search_kwargs["filter"] = {
            "source": {
                "$in": [
                    f"app/uploads/{pdf}"
                    for pdf in selected_documents
                ]
            }
        }

    vector_retriever = db.as_retriever(
        search_kwargs=search_kwargs
    )

    # -----------------------------
    # BM25 Retriever
    # -----------------------------
    if selected_documents:

        filtered_documents = [
            doc
            for doc in all_documents
            if os.path.basename(
                doc.metadata.get("source", "")
            ) in selected_documents
        ]

        print("Selected PDFs :", selected_documents)
        print("Matched Chunks:", len(filtered_documents))

    else:

        filtered_documents = all_documents

    # Safety check
    if len(filtered_documents) == 0:

        print("⚠ No matching documents found.")
        print("⚠ Falling back to ALL documents.")

        filtered_documents = all_documents

    bm25_retriever = BM25Retriever.from_documents(
        filtered_documents
    )

    bm25_retriever.k = 4

    # -----------------------------
    # Hybrid Retriever
    # -----------------------------
    hybrid_retriever = EnsembleRetriever(
        retrievers=[
            vector_retriever,
            bm25_retriever
        ],
        weights=[
            0.5,
            0.5
        ]
    )

    return hybrid_retriever