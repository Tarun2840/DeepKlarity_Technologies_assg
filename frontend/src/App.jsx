import React, { useState } from "react";
import GenerateQuizTab from "./tabs/GenerateQuizTab";
import HistoryTab from "./tabs/HistoryTab";
import "./index.css";

function App() {
  const [activeTab, setActiveTab] = useState("generate");

  return (
    <div>
      <h1 className="app-title">AI Wiki Quiz Generator</h1>
      <div className="tabs">
        <button
          className={activeTab === "generate" ? "active" : ""}
          onClick={() => setActiveTab("generate")}
        >
          Generate Quiz
        </button>
        <button
          className={activeTab === "history" ? "active" : ""}
          onClick={() => setActiveTab("history")}
        >
          History
        </button>
      </div>
      <div className="tab-content">
        {activeTab === "generate" && <GenerateQuizTab />}
        {activeTab === "history" && <HistoryTab />}
      </div>
    </div>
  );
}

export default App;
