import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import {
    getHistory,
    deleteHistory
} from "../services/historyService";

interface ChatHistory {
    id: number;
    question: string;
    answer: string;
}

function HistoryPage() {

    const [history, setHistory] =

        useState<ChatHistory[]>([]);

    const [loading, setLoading] =

        useState(true);

    useEffect(() => {

        loadHistory();

    }, []);

    async function loadHistory() {

        try {

            const data = await getHistory();

            setHistory(data);

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setLoading(false);

        }

    }

    async function handleDelete(

        id: number

    ) {

        const confirmDelete = window.confirm(

            "Delete this conversation?"

        );

        if (!confirmDelete) return;

        await deleteHistory(id);

        setHistory(prev =>

            prev.filter(chat => chat.id !== id)

        );

    }

    return (

        <DashboardLayout>

            <h1 className="text-3xl font-bold mb-8">

                Chat History

            </h1>

            {

                loading ?

                (

                    <p>

                        Loading...

                    </p>

                )

                :

                history.length === 0 ?

                (

                    <div className="bg-white p-6 rounded shadow">

                        No conversations yet.

                    </div>

                )

                :

                (

                    <div className="space-y-4">

                        {

                            history.map(chat => (

                                <div

                                    key={chat.id}

                                    className="bg-white rounded-xl shadow p-5"

                                >

                                    <h2 className="font-bold text-lg">

                                        {chat.question}

                                    </h2>

                                    <p className="mt-3 text-gray-700">

                                        {

                                            chat.answer.length > 250

                                            ?

                                            chat.answer.substring(0,250)

                                            +"..."

                                            :

                                            chat.answer

                                        }

                                    </p>

                                    <div className="mt-5">

                                        <button

                                            onClick={()=>

                                                handleDelete(chat.id)

                                            }

                                            className="bg-red-600 hover:bg-red-700 text-white px-5 py-2 rounded"

                                        >

                                            Delete

                                        </button>

                                    </div>

                                </div>

                            ))

                        }

                    </div>

                )

            }

        </DashboardLayout>

    );

}

export default HistoryPage;