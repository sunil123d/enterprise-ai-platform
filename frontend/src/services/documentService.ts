const RAG_URL = import.meta.env.VITE_RAG_URL;



export async function uploadDocument(file: File) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(
        `${RAG_URL}/documents/upload`,
        {
            method: "POST",
            body: formData
        }
    );

    if (!response.ok) {
        throw new Error("Upload failed");
    }

    return await response.json();
}

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