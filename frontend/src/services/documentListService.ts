const RAG_URL = "http://localhost:8001";

export async function getDocuments() {

    const response = await fetch(
        `${RAG_URL}/documents`
    );

    if (!response.ok) {

        throw new Error("Failed to load documents");

    }

    return await response.json();

}

export async function deleteDocument(filename: string) {

    const response = await fetch(
        `${RAG_URL}/documents/${filename}`,
        {
            method: "DELETE"
        }
    );

    if (!response.ok) {

        throw new Error("Delete failed");

    }

    return await response.json();

}