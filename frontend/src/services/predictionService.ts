const API_URL = import.meta.env.VITE_API_URL;
export async function predictChurn(data: any) {

    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_URL}/predict/churn`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            },

            body: JSON.stringify(data)
        }
    );

    if (!response.ok) {
        throw new Error("Prediction failed");
    }

    return await response.json();
}