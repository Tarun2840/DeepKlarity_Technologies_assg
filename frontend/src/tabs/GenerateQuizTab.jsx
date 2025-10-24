import React, { useState } from "react";
import { generateQuiz } from "../services/api";

export default function GenerateQuizTab() {
  const [url, setUrl] = useState("");
  const [quizData, setQuizData] = useState(null);

  const handleGenerate = async () => {
    try {
      const data = await generateQuiz(url);
      setQuizData(data);
    } catch (err) {
      alert("Error generating quiz. Make sure backend is running!");
    }
  };

  return (
    <div>
      <h2>Generate Quiz</h2>
      <input
        type="text"
        placeholder="Wikipedia URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "400px", padding: "5px" }}
      />
      <button onClick={handleGenerate} style={{ marginLeft: "10px" }}>
        Generate Quiz
      </button>

      {quizData && (
        <div style={{ marginTop: "20px" }}>
          <h3>{quizData.title}</h3>
          <p>{quizData.summary}</p>
          {quizData.quiz.map((q, i) => (
            <div key={i} style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
              <strong>Q{i + 1}: {q.question}</strong>
              <ul>
                {q.options.map((opt, idx) => (
                  <li key={idx}>{opt}</li>
                ))}
              </ul>
              <p><strong>Answer:</strong> {q.answer}</p>
              <p><strong>Explanation:</strong> {q.explanation}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
