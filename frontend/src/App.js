import React, { useState } from "react";
const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [tab, setTab] = useState("results");

  const search = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setResult(null);
    try {
      const url = `${API_BASE}/search?q=${encodeURIComponent(query)}`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`Error ${res.status}`);
      const ct = res.headers.get("content-type") || "";
      if (!ct.includes("application/json")) throw new Error("Non‑JSON response");
      const data = await res.json();
      setResult(data);
      setTab("results");
    } catch (err) {
      alert("Search failed: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const sections = [
    { key: "refined", label: "Refined Query" },
    { key: "results", label: "Results" },
    { key: "hypothesis", label: "Hypothesis" },
    { key: "report", label: "Auto Report" },
  ];

  return (
    <div className="min-h-screen flex bg-gray-100 text-gray-800">
      {/* Sidebar */}
      <aside className="w-full md:w-1/4 bg-white shadow-md p-6 flex flex-col gap-6 sticky top-0 h-screen">
        <div>
          <h1 className="text-2xl font-bold text-blue-700">🧠 Research Agent</h1>
          <p className="text-sm text-gray-500">IBM Granite Powered</p>
        </div>

        <textarea
          rows="4"
          className="w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-blue-500 resize-none"
          placeholder="Enter your research question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
          disabled={loading}
          onClick={search}
        >
          {loading ? "Searching..." : "Search"}
        </button>

        {result && (
          <nav className="mt-4 flex flex-wrap gap-2">
            {sections.map((sec) => (
              <button
                key={sec.key}
                onClick={() => setTab(sec.key)}
                className={`px-3 py-1 rounded ${
                  tab === sec.key
                    ? "bg-blue-600 text-white"
                    : "bg-blue-100 text-blue-700 hover:bg-blue-200"
                }`}
              >
                {sec.label}
              </button>
            ))}
          </nav>
        )}
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto p-6 space-y-8">
        {!result && (
          <div className="mt-20 text-center text-gray-500">
            Ask a question to get started.
          </div>
        )}

        {result && tab === "refined" && (
          <section>
            <h2 className="text-xl font-semibold mb-2">🔍 Refined Query</h2>
            <p className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
              {result.refined_query}
            </p>
          </section>
        )}

        {result && tab === "results" && (
          <section>
            <h2 className="text-xl font-semibold mb-4">📄 Search Results</h2>
            <div className="space-y-6">
              {result.results.map((paper, i) => (
                <div
                  key={i}
                  className="bg-white rounded-lg shadow hover:shadow-lg transition p-5 space-y-3"
                >
                  <h3 className="text-lg font-bold text-blue-800">
                    {paper.title}
                  </h3>
                  <p className="text-sm text-gray-600">
                    Authors: {paper.authors.join(", ")}
                  </p>
                  <p>{paper.summary_granite}</p>
                  <details className="mt-3">
                    <summary className="cursor-pointer text-blue-600">
                      📚 Citations
                    </summary>
                    <pre className="bg-gray-100 p-3 rounded text-sm overflow-auto whitespace-pre-wrap break-words max-h-60 border mt-2">
APA: {paper.citations.APA}

IEEE: {paper.citations.IEEE}

BibTeX:
{paper.citations.BibTeX}
                    </pre>
                  </details>
                  <a
                    href={paper.link}
                    target="_blank"
                    rel="noreferrer"
                    className="text-blue-500 hover:underline text-sm"
                  >
                    View on arXiv →
                  </a>
                </div>
              ))}
            </div>
          </section>
        )}

        {result && tab === "hypothesis" && (
          <section>
            <h2 className="text-xl font-semibold mb-2">💡 Suggested Hypothesis</h2>
            <p className="bg-yellow-50 border-l-4 border-yellow-400 p-4 rounded">
              {result.generated_hypothesis}
            </p>
          </section>
        )}

        {result && tab === "report" && (
          <section className="space-y-6">
            <h2 className="text-xl font-semibold mb-4">📘 Full Report</h2>
            {Object.entries(result.auto_generated_report).map(
              ([section, content]) => (
                <div key={section}>
                  <h3 className="text-lg font-bold text-blue-700">
                    {section}
                  </h3>
                  <p className="whitespace-pre-line">{content}</p>
                </div>
              )
            )}
          </section>
        )}
      </main>
    </div>
  );
}

export default App;
