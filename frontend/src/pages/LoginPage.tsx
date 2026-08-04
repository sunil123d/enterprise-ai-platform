import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { login } from "../services/authService";

function LoginPage() {
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleLogin() {
        alert("Login button clicked");

        console.log("Email:", email);
        console.log("Password:", password);

        if (!email || !password) {
            alert("Please enter email and password.");
            return;
        }

        try {
            setLoading(true);

            const data = await login(email, password);

            console.log("Backend Response:", data);
            alert(JSON.stringify(data));

            localStorage.setItem(
                "token",
                data.access_token
            );

            alert("Login Successful");

            navigate("/dashboard");
        } catch (error: any) {
            console.error("Login Error:", error);

            if (error.response) {
                console.log("Status:", error.response.status);
                console.log("Response:", error.response.data);

                alert(
                    JSON.stringify(error.response.data)
                );
            } else {
                alert("Unable to connect to backend.");
            }
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-slate-100">
            <div className="bg-white p-8 rounded-xl shadow-lg w-96">

                <h1 className="text-3xl font-bold text-center mb-6">
                    Enterprise AI Login
                </h1>

                <input
                    type="email"
                    placeholder="Email"
                    className="border p-3 w-full mb-4 rounded"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    className="border p-3 w-full mb-6 rounded"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button
                    onClick={handleLogin}
                    disabled={loading}
                    className="bg-blue-600 text-white w-full p-3 rounded hover:bg-blue-700 disabled:bg-gray-400"
                >
                    {loading ? "Logging in..." : "Login"}
                </button>

            </div>
        </div>
    );
}

export default LoginPage;