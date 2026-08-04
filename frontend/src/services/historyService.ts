const API_URL = "http://localhost:8000";

export interface ChatHistory {
    id: number;
    question: string;
    answer: string;
}

export async function getHistory() {
    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_URL}/chat/history`,
        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    );

    if (!response.ok) {
        throw new Error("Failed to load history");
    }

    return await response.json();
}

export async function deleteHistory(id: number) {
    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_URL}/chat/${id}`,
        {
            method: "DELETE",
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    );

    if (!response.ok) {
        throw new Error("Delete failed");
    }

    return await response.json();
}