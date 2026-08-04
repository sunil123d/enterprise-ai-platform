import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";

import {
    getDocuments,
    deleteDocument
} from "../services/documentListService";

interface DocumentItem {
    filename: string;
}

function DocumentsPage() {

    const navigate = useNavigate();

    const [documents, setDocuments] = useState<DocumentItem[]>([]);
    const [selectedDocuments, setSelectedDocuments] = useState<string[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadDocuments();
    }, []);

    async function loadDocuments() {

        try {

            const data = await getDocuments();

            setDocuments(data);

        } catch (error) {

            console.error(error);

            alert("Failed to load documents");

        } finally {

            setLoading(false);

        }

    }

    function toggleDocument(filename: string) {

        setSelectedDocuments(prev => {

            if (prev.includes(filename)) {

                return prev.filter(doc => doc !== filename);

            }

            return [...prev, filename];

        });

    }

    async function handleDelete(filename: string) {

        const confirmDelete = window.confirm(
            `Delete "${filename}" ?`
        );

        if (!confirmDelete) return;

        try {

            await deleteDocument(filename);

            setDocuments(prev =>
                prev.filter(doc => doc.filename !== filename)
            );

            setSelectedDocuments(prev =>
                prev.filter(doc => doc !== filename)
            );

            alert("Document deleted successfully.");

        } catch (error) {

            console.error(error);

            alert("Delete failed.");

        }

    }

    function handleChat() {

        // Save selected PDFs (can be empty)
        localStorage.setItem(
            "selectedDocuments",
            JSON.stringify(selectedDocuments)
        );

        navigate("/chat");

    }

    return (

        <DashboardLayout>

            <h1 className="text-3xl font-bold mb-8">

                Uploaded Documents

            </h1>

            {

                loading ?

                    <p>Loading...</p>

                    :

                    documents.length === 0 ?

                        <div className="bg-white p-6 rounded shadow">

                            <p className="mb-4">
                                No documents uploaded.
                            </p>

                            <button
                                onClick={handleChat}
                                className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded"
                            >
                                🌐 Continue with General AI Chat
                            </button>

                        </div>

                        :

                        <>

                            <div className="space-y-4">

                                {

                                    documents.map((doc) => (

                                        <div

                                            key={doc.filename}

                                            className="bg-white p-4 rounded shadow flex justify-between items-center"

                                        >

                                            <span className="font-medium">

                                                📄 {doc.filename}

                                            </span>

                                            <div className="flex items-center gap-4">

                                                <input

                                                    type="checkbox"

                                                    checked={
                                                        selectedDocuments.includes(
                                                            doc.filename
                                                        )
                                                    }

                                                    onChange={() =>
                                                        toggleDocument(
                                                            doc.filename
                                                        )
                                                    }

                                                />

                                                <button

                                                    onClick={() =>
                                                        handleDelete(
                                                            doc.filename
                                                        )
                                                    }

                                                    className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded"

                                                >

                                                    Delete

                                                </button>

                                            </div>

                                        </div>

                                    ))

                                }

                            </div>

                            <div className="mt-8">

                                <p className="font-semibold mb-4">

                                    Selected Documents: {selectedDocuments.length}

                                </p>

                                {

                                    selectedDocuments.length === 0 ?

                                        <p className="text-green-600 mb-4">

                                            🌐 No document selected. Chat will use General AI Mode.

                                        </p>

                                        :

                                        <p className="text-blue-600 mb-4">

                                            📄 Chat will use the selected documents.

                                        </p>

                                }

                                <button

                                    onClick={handleChat}

                                    className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded"

                                >

                                    💬 Start Chat

                                </button>

                            </div>

                        </>

            }

        </DashboardLayout>

    );

}

export default DocumentsPage;