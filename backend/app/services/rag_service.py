import httpx

RAG_URL = "http://localhost:8001/chat"


async def ask_rag(question: str):

    async with httpx.AsyncClient(timeout=60) as client:

        response = await client.post(
            RAG_URL,
            json={
                "question": question
            }
        )

        response.raise_for_status()

        return response.json()