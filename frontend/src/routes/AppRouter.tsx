import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";
import DashboardPage from "../pages/DashboardPage";
import UploadPage from "../pages/UploadPage";
import DocumentsPage from "../pages/DocumentsPage";
import ChatPage from "../pages/ChatPage";
import ProfilePage from "../pages/ProfilePage";
import PredictionPage from "../pages/PredictionPage";
import HistoryPage from "../pages/HistoryPage";




function AppRouter() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<LoginPage />}
                />

                <Route
                    path="/register"
                    element={<RegisterPage />}
                />

                <Route
                    path="/dashboard"
                    element={<DashboardPage />}
                />

                <Route
                    path="/prediction"
                    element={<PredictionPage />}
                />

                <Route
                    path="/upload"
                    element={<UploadPage />}
                />

                <Route
                    path="/documents"
                    element={<DocumentsPage />}
                />

                <Route
                    path="/chat"
                    element={<ChatPage />}
                />
                <Route
                    path="/history"
                    element={<HistoryPage />}
                />
                <Route
                    path="/profile"
                    element={<ProfilePage />}
                />

            </Routes>

        </BrowserRouter>

    );

}

export default AppRouter;