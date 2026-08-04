import { useNavigate } from "react-router-dom";

function Sidebar() {

    const navigate = useNavigate();

    return (
        <div className="w-64 h-screen bg-slate-900 text-white p-6">

            <h1 className="text-2xl font-bold mb-10">
                Enterprise AI
            </h1>

            <nav className="flex flex-col gap-4">

                <button
                    onClick={() => navigate("/upload")}
                    className="text-left hover:text-blue-400"
                >
                    📤 Upload
                </button>

                <button
                    onClick={() => navigate("/documents")}
                    className="text-left hover:text-blue-400"
                >
                    📄 Documents
                </button>

                <button
                    onClick={() => navigate("/chat")}
                    className="text-left hover:text-blue-400"
                >
                    💬 Chat
                </button>

                <button
                    onClick={() => navigate("/history")}
                    className="text-left hover:text-blue-400"
                >
                    📜 History
                </button>

                <button
                    onClick={() => navigate("/prediction")}
                    className="text-left hover:text-blue-400"
                >
                    📊 Prediction
                </button>

                <button
                    onClick={() => navigate("/profile")}
                    className="text-left hover:text-blue-400"
                >
                    👤 Profile
                </button>

                <button
                    onClick={() => navigate("/")}
                    className="text-left text-red-400 hover:text-red-300 mt-8"
                >
                    🚪 Logout
                </button>

            </nav>

        </div>
    );
}

export default Sidebar;