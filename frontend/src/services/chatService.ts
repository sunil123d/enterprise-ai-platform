const API_URL = "http://localhost:8000";

export async function askQuestion(
    question: string,
    documents: string[],
    history: any[]
) {
    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_URL}/chat`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({
                question,
                documents,
                history,
            }),
        }
    );

    if (!response.ok) {
        throw new Error("Chat failed");
    }

    return await response.json();
}