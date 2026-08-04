import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";
import { getProfile } from "../services/profileService";

function ProfilePage() {

    const [profile, setProfile] = useState<any>(null);

    useEffect(() => {

        async function loadProfile() {

            try {

                const data = await getProfile();

                setProfile(data);

            } catch (error) {

                console.error(error);

            }

        }

        loadProfile();

    }, []);

    return (

        <DashboardLayout>

            <h1 className="text-3xl font-bold mb-8">
                My Profile
            </h1>

            {!profile ? (

                <p>Loading...</p>

            ) : (

                <div className="bg-white p-8 rounded shadow space-y-4">

                    <p>
                        <strong>ID:</strong> {profile.id}
                    </p>

                    <p>
                        <strong>Name:</strong> {profile.full_name}
                    </p>

                    <p>
                        <strong>Email:</strong> {profile.email}
                    </p>

                    <p>
                        <strong>Role:</strong> {profile.role}
                    </p>

                    <p>
                        <strong>Active:</strong> {profile.is_active ? "Yes" : "No"}
                    </p>

                </div>

            )}

        </DashboardLayout>

    );

}

export default ProfilePage;