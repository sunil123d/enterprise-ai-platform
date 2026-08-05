const API_URL = import.meta.env.VITE_API_URL;
export async function getProfile() {
    const response = await fetch(`${API_URL}/profile`);

    if (!response.ok) {
        throw new Error("Failed to load profile");
    }

    return await response.json();
}