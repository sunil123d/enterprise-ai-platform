interface Option {

    label: string;

    value: number;

}

interface Props {

    label: string;

    name: string;

    value: number;

    type?: "text" | "number" | "select";

    options?: Option[];

    onChange: (
        e: React.ChangeEvent<
            HTMLInputElement |
            HTMLSelectElement
        >
    ) => void;

}

function FormField({

    label,

    name,

    value,

    type = "select",

    options = [],

    onChange

}: Props) {

    return (

        <div>

            <label className="block font-semibold mb-2">

                {label}

            </label>

            {

                type === "select"

                ?

                <select

                    name={name}

                    value={value}

                    onChange={onChange}

                    className="w-full border rounded-lg p-3"

                >

                    {

                        options.map(option => (

                            <option

                                key={option.value}

                                value={option.value}

                            >

                                {option.label}

                            </option>

                        ))

                    }

                </select>

                :

                <input

                    type="number"

                    name={name}

                    value={value}

                    onChange={onChange}

                    className="w-full border rounded-lg p-3"

                />

            }

        </div>

    );

}

export default FormField;