from langchain_ollama import OllamaEmbeddings


def get_embeddings():

    return OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="http://host.docker.internal:11434"
    )