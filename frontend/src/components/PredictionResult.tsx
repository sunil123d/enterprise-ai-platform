interface Props {

    prediction: number;

    probability: number;

}

function PredictionResult({

    prediction,

    probability

}: Props) {

    const percent = (probability * 100).toFixed(2);

    const highRisk = prediction === 1;

    return (

        <div className="bg-white rounded-xl shadow-lg p-8 mt-8">

            <h2 className="text-2xl font-bold mb-6">

                Prediction Result

            </h2>

            <div className="flex items-center gap-4 mb-6">

                <div

                    className={`px-5 py-2 rounded-full text-white font-bold

                    ${highRisk

                        ? "bg-red-600"

                        : "bg-green-600"

                    }`}

                >

                    {

                        highRisk

                            ? "🔴 High Churn Risk"

                            : "🟢 Low Churn Risk"

                    }

                </div>

            </div>

            <div className="mb-6">

                <p className="font-semibold mb-2">

                    Probability

                </p>

                <div className="w-full bg-gray-200 rounded-full h-4">

                    <div

                        className={`h-4 rounded-full

                        ${highRisk

                            ? "bg-red-500"

                            : "bg-green-500"

                        }`}

                        style={{

                            width: `${percent}%`

                        }}

                    />

                </div>

                <p className="mt-2 text-lg font-bold">

                    {percent}%

                </p>

            </div>

            <div className="mb-6">

                <p className="font-semibold">

                    Model Used

                </p>

                <p>

                    XGBoost

                </p>

            </div>

            <div>

                <p className="font-semibold mb-2">

                    Recommendation

                </p>

                {

                    highRisk ?

                    <div className="bg-red-50 border border-red-300 rounded-lg p-4">

                        <ul className="list-disc ml-5 space-y-2">

                            <li>Offer a long-term contract discount.</li>

                            <li>Contact the customer proactively.</li>

                            <li>Provide loyalty rewards.</li>

                            <li>Review recent complaints and service quality.</li>

                        </ul>

                    </div>

                    :

                    <div className="bg-green-50 border border-green-300 rounded-lg p-4">

                        <ul className="list-disc ml-5 space-y-2">

                            <li>Customer is likely to stay.</li>

                            <li>Recommend premium services.</li>

                            <li>Offer cross-selling opportunities.</li>

                            <li>Continue regular engagement.</li>

                        </ul>

                    </div>

                }

            </div>

        </div>

    );

}

export default PredictionResult;