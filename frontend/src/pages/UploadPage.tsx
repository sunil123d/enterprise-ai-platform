import { useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import { uploadDocument } from "../services/documentService";

function UploadPage() {

    const [file, setFile] = useState<File | null>(null);

    const [loading, setLoading] = useState(false);

async function handleUpload() {

    console.log("===== Upload Button Clicked =====");

    if (!file) {
        console.log("No file selected");
        alert("Please choose a PDF.");
        return;
    }

    console.log("Selected File:", file);

    try {

        setLoading(true);

        const result = await uploadDocument(file);

        console.log("Upload Success:", result);

        alert(result.message);

    } catch (error) {

        console.error("Upload Error:", error);

        alert("Upload Failed");

    } finally {

        setLoading(false);

    }

}

    return (

        <DashboardLayout>

            <h1 className="text-3xl font-bold mb-8">

                Upload PDF

            </h1>

            <div className="bg-white p-8 rounded-xl shadow">

<input
    type="file"
    accept=".pdf"
    onChange={(e) => {

        console.log("onChange fired");

        if (e.target.files && e.target.files.length > 0) {

            console.log("Selected File:", e.target.files[0]);

            setFile(e.target.files[0]);

        } else {

            console.log("No file selected from input");

        }

    }}
/>

                <br />

                <button

                    onClick={handleUpload}

                    disabled={loading}

                    className="mt-6 bg-blue-600 text-white px-6 py-3 rounded"

                >

                    {

                        loading

                        ?

                        "Uploading..."

                        :

                        "Upload"

                    }

                </button>

            </div>

        </DashboardLayout>

    );

}

export default UploadPage;