import { useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";
import Message from "../components/Message";
import { askQuestion } from "../services/chatService";

interface Source {
    page: number | null;
    source: string | null;
}

interface ChatMessage {
    role: "user" | "assistant";
    content: string;
    sources?: Source[];
}

interface HistoryItem {
    question: string;
    answer: string;
}

function ChatPage() {

    const documents = JSON.parse(
        localStorage.getItem("selectedDocuments") || "[]"
    );

    const [question, setQuestion] = useState("");

    const [messages, setMessages] = useState<ChatMessage[]>([]);

    const [history, setHistory] = useState<HistoryItem[]>([]);

    const [loading, setLoading] = useState(false);

    async function handleSend() {

        if (!question.trim()) {

            alert("Please enter a question");

            return;

        }

        const currentQuestion = question;

        setMessages(prev => [

            ...prev,

            {

                role: "user",

                content: currentQuestion

            }

        ]);

        setQuestion("");

        setLoading(true);

        try {

            const response = await askQuestion(

                currentQuestion,

                documents,

                history

            );

            setMessages(prev => [

                ...prev,

                {

                    role: "assistant",

                    content: response.answer,

                    sources: response.sources

                }

            ]);

            // Save conversation memory
            setHistory(prev => [

                ...prev,

                {

                    question: currentQuestion,

                    answer: response.answer

                }

            ]);

        }

        catch (error) {

            console.error(error);

            alert("Failed to get response");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <DashboardLayout>

            <h1 className="text-3xl font-bold mb-6">

                Enterprise AI Chat

            </h1>

            <div className="bg-white rounded shadow p-5 mb-5">

                <h2 className="font-semibold mb-3">

                    Selected Documents

                </h2>

                {

                    documents.length === 0 ?

                        <p className="text-green-700">

                            🌐 General AI Mode (No PDF Selected)

                        </p>

                        :

                        documents.map((doc: string) => (

                            <div
                                key={doc}
                                className="mb-2"
                            >

                                📄 {doc}

                            </div>

                        ))

                }

            </div>

            <div className="bg-slate-100 rounded-xl p-5 h-[500px] overflow-y-auto">

                {

                    messages.length === 0 &&

                    <div className="text-gray-500">

                        {

                            documents.length === 0

                                ?

                                "Ask me anything..."

                                :

                                "Ask a question about your uploaded documents."

                        }

                    </div>

                }

                {

                    messages.map((msg, index) => (

                        <Message

                            key={index}

                            role={msg.role}

                            content={msg.content}

                            sources={msg.sources}

                        />

                    ))

                }

                {

                    loading &&

                    <div className="mt-4 text-gray-500 animate-pulse">

                        🤖 Thinking...

                    </div>

                }

            </div>

            <div className="mt-5 flex gap-3">

                <textarea

                    className="border rounded-lg w-full p-3"

                    rows={3}

                    placeholder={

                        documents.length === 0

                            ?

                            "Ask anything..."

                            :

                            "Ask anything about your documents..."

                    }

                    value={question}

                    onChange={
                        e => setQuestion(e.target.value)
                    }

                />

                <button

                    onClick={handleSend}

                    disabled={loading}

                    className="bg-blue-600 hover:bg-blue-700 text-white px-8 rounded-lg"

                >

                    Send

                </button>

            </div>

        </DashboardLayout>

    );

}

export default ChatPage;