import { useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import PredictionForm from "../components/PredictionForm";
import PredictionResult from "../components/PredictionResult";

import { predictChurn } from "../services/predictionService";

import type {
    PredictionFormData,
    PredictionResponse
} from "../types/prediction";

function PredictionPage() {

    const [form, setForm] = useState<PredictionFormData>({

        gender: 1,

        SeniorCitizen: 0,

        Partner: 1,

        Dependents: 0,

        tenure: 12,

        PhoneService: 1,

        MultipleLines: 0,

        InternetService: 1,

        OnlineSecurity: 0,

        OnlineBackup: 0,

        DeviceProtection: 0,

        TechSupport: 0,

        StreamingTV: 0,

        StreamingMovies: 0,

        Contract: 0,

        PaperlessBilling: 1,

        PaymentMethod: 2,

        MonthlyCharges: 70,

        TotalCharges: 840

    });

    const [loading, setLoading] = useState(false);

    const [result, setResult] =
        useState<PredictionResponse | null>(null);

    function handleChange(

        e: React.ChangeEvent<
            HTMLInputElement |
            HTMLSelectElement
        >

    ) {

        const { name, value } = e.target;

        setForm(prev => ({

            ...prev,

            [name]: Number(value)

        }));

    }

    async function handlePredict() {

        try {

            setLoading(true);

            const response = await predictChurn(form);

            setResult(response);

        }

        catch (error) {

            console.error(error);

            alert("Prediction Failed");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <DashboardLayout>

            <div className="max-w-6xl mx-auto">

                <h1 className="text-4xl font-bold mb-8">

                    Customer Churn Prediction

                </h1>

                <PredictionForm

                    form={form}

                    loading={loading}

                    onChange={handleChange}

                    onSubmit={handlePredict}

                />

                {

                    result && (

                        <PredictionResult

                            prediction={result.prediction}

                            probability={result.probability}

                        />

                    )

                }

            </div>

        </DashboardLayout>

    );

}

export default PredictionPage;