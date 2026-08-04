const API_URL = "http://localhost:8000";

export async function getProfile() {
    const response = await fetch(`${API_URL}/profile`);

    if (!response.ok) {
        throw new Error("Failed to load profile");
    }

    return await response.json();
}