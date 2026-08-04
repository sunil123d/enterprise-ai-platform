import DashboardLayout from "../layouts/DashboardLayout";

function DashboardPage() {

    return (

        <DashboardLayout>

            <h1 className="text-3xl font-bold">
                Welcome to Enterprise AI
            </h1>

            <p className="mt-4 text-gray-600">
                Upload documents and start chatting with your AI assistant.
            </p>

        </DashboardLayout>

    );

}

export default DashboardPage;