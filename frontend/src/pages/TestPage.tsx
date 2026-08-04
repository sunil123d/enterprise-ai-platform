function TestPage() {

    return (
        <div style={{ padding: 50 }}>

            <input
                type="file"
                onChange={() => console.log("FILE CHANGED")}
            />

            <br /><br />

            <button
                onClick={() => alert("Button Works")}
            >
                Click Me
            </button>

        </div>
    );
}

export default TestPage;