import { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [pdfFile, setPdfFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [summaryLength, setSummaryLength] = useState("medium");

  const handleSummarize = async () => {
  try {

    setLoading(true);

    const response = await axios.post(
      "http://127.0.0.1:8000/summarize",
      {
        text: text,
        length: summaryLength
      }
    );

    setSummary(response.data.summary);

  } catch (error) {

    console.error(error);
    alert("Error connecting to backend");

  } finally {

    setLoading(false);

  }
};
  const handlePdfUpload = async () => {

  if (!pdfFile) {
    alert("Select a PDF first");
    return;
  }

  try {

    setLoading(true);

    const formData = new FormData();

    formData.append("file", pdfFile);
    formData.append("length", summaryLength);

    const response = await axios.post(
      "http://127.0.0.1:8000/summarize-pdf",
      formData
    );

    setSummary(response.data.summary);

  } catch (error) {

    console.error(error);
    alert("Error uploading PDF");

  } finally {

    setLoading(false);

  }
};

  return (
    <div style={{ padding: "30px" }}>
      <h1>AI Text Summarizer</h1>

      <textarea
        rows="10"
        cols="60"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text here..."
      />

      <br /><br />

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setPdfFile(e.target.files[0])}
      />

      <br /><br />

      <select
        value={summaryLength}
        onChange={(e) => setSummaryLength(e.target.value)}
      >
        <option value="short">Short Summary</option>
        <option value="medium">Medium Summary</option>
        <option value="long">Long Summary</option>
      </select>

      <br /><br />

      <button onClick={handleSummarize}>
        Summarize
      </button>
      <button onClick={handlePdfUpload}>
        Summarize PDF
      </button>
      {loading && <p>Generating summary...</p>}
      <h2>Summary</h2>
      <p>{summary}</p>
    </div>
  );
}

export default App;