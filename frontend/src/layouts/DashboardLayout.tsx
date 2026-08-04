import type { ReactNode } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

interface Props {
    children: ReactNode;
}

function DashboardLayout({ children }: Props) {

    return (

        <div className="flex">

            <Sidebar />

            <div className="flex-1 bg-slate-100 min-h-screen">

                <Navbar />

                <div className="p-8">

                    {children}

                </div>

            </div>

        </div>

    );

}

export default DashboardLayout;