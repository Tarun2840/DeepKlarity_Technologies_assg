# llm_quiz_generator.py
def generate_quiz(topic: str):
    """
    Mock function to simulate quiz generation.
    Later, this will use LangChain + Gemini/OpenAI API.
    """
    sample_quiz = {
        "topic": topic,
        "questions": [
            {
                "question": f"What is {topic}?",
                "options": ["A concept", "A tool", "A process", "None of the above"],
                "answer": "A concept"
            },
            {
                "question": f"Who invented {topic}?",
                "options": ["Newton", "Einstein", "Alan Turing", "Unknown"],
                "answer": "Alan Turing"
            }
        ]
    }
    return sample_quiz
