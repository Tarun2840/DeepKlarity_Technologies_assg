export default function QuizDisplay({ quiz }) {
  return (
    <div>
      {quiz.map((q, idx) => (
        <div key={idx} className="quiz-card">
          <strong>{idx + 1}. {q.question}</strong>
          <ul>
            {q.options.map((opt, i) => (
              <li key={i}>{opt}</li>
            ))}
          </ul>
          <p><strong>Answer:</strong> {q.answer}</p>
          <p><strong>Explanation:</strong> {q.explanation}</p>
          <p><strong>Difficulty:</strong> {q.difficulty}</p>
        </div>
      ))}
    </div>
  );
}
