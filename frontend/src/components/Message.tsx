import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

interface Source {

    page: number | null;

    source: string | null;

}

interface Props {

    role: "user" | "assistant";

    content: string;

    sources?: Source[];

}

function Message({

    role,

    content,

    sources

}: Props) {

    return (

        <div
            className={`mb-6 ${
                role === "user"
                    ? "text-right"
                    : "text-left"
            }`}
        >

            <div
                className={`inline-block max-w-[80%] p-4 rounded-xl ${
                    role === "user"
                        ? "bg-blue-600 text-white"
                        : "bg-white shadow"
                }`}
            >

                {

                    role === "assistant"

                        ?

                        <ReactMarkdown
                            remarkPlugins={[remarkGfm]}
                        >
                            {content}
                        </ReactMarkdown>

                        :

                        content

                }

            </div>

            {

                role === "assistant" &&
                sources &&

                <div className="text-sm text-gray-500 mt-2">

                    <b>Sources</b>

                    {

                        sources.map((s, index) => (

                            <div key={index}>

                                📄 {s.source} Page {s.page}

                            </div>

                        ))

                    }

                </div>

            }

        </div>

    );

}

export default Message;