export interface PredictionFormData {

    gender: number;

    SeniorCitizen: number;

    Partner: number;

    Dependents: number;

    tenure: number;

    PhoneService: number;

    MultipleLines: number;

    InternetService: number;

    OnlineSecurity: number;

    OnlineBackup: number;

    DeviceProtection: number;

    TechSupport: number;

    StreamingTV: number;

    StreamingMovies: number;

    Contract: number;

    PaperlessBilling: number;

    PaymentMethod: number;

    MonthlyCharges: number;

    TotalCharges: number;

}

export interface PredictionResponse {

    prediction: number;

    probability: number;

}