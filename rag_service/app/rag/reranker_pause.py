from sentence_transformers import CrossEncoder


# Load once when the application starts
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(question, documents, top_k=5):

    if not documents:
        return []

    pairs = [
        (question, doc.page_content)
        for doc in documents
    ]

    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, documents),
        key=lambda x: x[0],
        reverse=True
    )

    return [
        doc
        for _, doc in ranked[:top_k]
    ]