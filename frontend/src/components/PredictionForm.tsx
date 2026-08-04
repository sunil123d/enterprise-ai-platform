import FormField from "./FormField";

import {
    yesNo,
    gender,
    multipleLines,
    internetService,
    internetOptions,
    contract,
    paymentMethod
} from "../utils/predictionOptions";

import type { PredictionFormData } from "../types/prediction";

interface Props {

    form: PredictionFormData;

    loading: boolean;

    onChange: (
        e: React.ChangeEvent<
            HTMLInputElement |
            HTMLSelectElement
        >
    ) => void;

    onSubmit: () => void;

}

function PredictionForm({

    form,

    loading,

    onChange,

    onSubmit

}: Props) {

    return (

        <div className="bg-white rounded-xl shadow-lg p-8">

            <div className="grid md:grid-cols-2 gap-6">

                <FormField
                    label="Gender"
                    name="gender"
                    value={form.gender}
                    options={gender}
                    onChange={onChange}
                />

                <FormField
                    label="Senior Citizen"
                    name="SeniorCitizen"
                    value={form.SeniorCitizen}
                    options={yesNo}
                    onChange={onChange}
                />

                <FormField
                    label="Partner"
                    name="Partner"
                    value={form.Partner}
                    options={yesNo}
                    onChange={onChange}
                />

                <FormField
                    label="Dependents"
                    name="Dependents"
                    value={form.Dependents}
                    options={yesNo}
                    onChange={onChange}
                />

                <FormField
                    label="Phone Service"
                    name="PhoneService"
                    value={form.PhoneService}
                    options={yesNo}
                    onChange={onChange}
                />

                <FormField
                    label="Multiple Lines"
                    name="MultipleLines"
                    value={form.MultipleLines}
                    options={multipleLines}
                    onChange={onChange}
                />

                <FormField
                    label="Internet Service"
                    name="InternetService"
                    value={form.InternetService}
                    options={internetService}
                    onChange={onChange}
                />

                <FormField
                    label="Online Security"
                    name="OnlineSecurity"
                    value={form.OnlineSecurity}
                    options={internetOptions}
                    onChange={onChange}
                />

                <FormField
                    label="Online Backup"
                    name="OnlineBackup"
                    value={form.OnlineBackup}
                    options={internetOptions}
                    onChange={onChange}
                />

                <FormField
                    label="Device Protection"
                    name="DeviceProtection"
                    value={form.DeviceProtection}
                    options={internetOptions}
                    onChange={onChange}
                />

                <FormField
                    label="Tech Support"
                    name="TechSupport"
                    value={form.TechSupport}
                    options={internetOptions}
                    onChange={onChange}
                />

                <FormField
                    label="Streaming TV"
                    name="StreamingTV"
                    value={form.StreamingTV}
                    options={internetOptions}
                    onChange={onChange}
                />

                <FormField
                    label="Streaming Movies"
                    name="StreamingMovies"
                    value={form.StreamingMovies}
                    options={internetOptions}
                    onChange={onChange}
                />

                <FormField
                    label="Contract"
                    name="Contract"
                    value={form.Contract}
                    options={contract}
                    onChange={onChange}
                />

                <FormField
                    label="Paperless Billing"
                    name="PaperlessBilling"
                    value={form.PaperlessBilling}
                    options={yesNo}
                    onChange={onChange}
                />

                <FormField
                    label="Payment Method"
                    name="PaymentMethod"
                    value={form.PaymentMethod}
                    options={paymentMethod}
                    onChange={onChange}
                />

                <FormField
                    label="Tenure"
                    name="tenure"
                    type="number"
                    value={form.tenure}
                    onChange={onChange}
                />

                <FormField
                    label="Monthly Charges"
                    name="MonthlyCharges"
                    type="number"
                    value={form.MonthlyCharges}
                    onChange={onChange}
                />

                <FormField
                    label="Total Charges"
                    name="TotalCharges"
                    type="number"
                    value={form.TotalCharges}
                    onChange={onChange}
                />

            </div>

            <button

                onClick={onSubmit}

                disabled={loading}

                className="mt-8 w-full bg-blue-600 hover:bg-blue-700 text-white rounded-lg py-4 text-lg"

            >

                {

                    loading

                        ? "Predicting..."

                        : "Predict Customer Churn"

                }

            </button>

        </div>

    );

}

export default PredictionForm;