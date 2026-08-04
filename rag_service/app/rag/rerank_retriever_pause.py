from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from pydantic import Field

from app.rag.hybrid_retriever import get_hybrid_retriever
from rag_service.app.rag.reranker_pause import rerank


class RerankRetriever(BaseRetriever):

    selected_documents: list[str] = Field(default_factory=list)

    def _get_relevant_documents(self, query: str) -> list[Document]:
        # Get hybrid retriever
        hybrid = get_hybrid_retriever(self.selected_documents)

        # Retrieve more chunks initially
        documents = hybrid.invoke(query)

        # Rerank and keep the best 5
        documents = rerank(
            question=query,
            documents=documents,
            top_k=5
        )

        return documents