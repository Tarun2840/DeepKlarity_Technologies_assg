import React, { useEffect, useState } from "react";
import { fetchHistory } from "../services/api";

export default function HistoryTab() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetchHistory().then(setHistory);
  }, []);

  return (
    <div>
      <h2>History</h2>
      {history.length === 0 ? (
        <p>No history yet.</p>
      ) : (
        <ul>
          {history.map((item) => (
            <li key={item.id}>
              {item.title} - {item.url}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
