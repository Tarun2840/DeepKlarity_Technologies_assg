from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins, adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class QuizRequest(BaseModel):
    url: str

# Quiz response models
class QuizItem(BaseModel):
    question: str
    options: List[str]
    answer: str
    explanation: str

class QuizResponse(BaseModel):
    title: str
    summary: str
    quiz: List[QuizItem]
    related_topics: List[str]

# In-memory history store
history = []

# Generate quiz endpoint (mock)
@app.post("/generate_quiz", response_model=QuizResponse)
def generate_quiz(req: QuizRequest):
    # Mock data
    quiz = [
        QuizItem(
            question="Who is Alan Turing?",
            options=["Mathematician", "Painter", "Singer", "Actor"],
            answer="Mathematician",
            explanation="Alan Turing was a mathematician and computer scientist."
        )
    ]
    result = QuizResponse(
        title="Alan Turing",
        summary="Alan Turing was a pioneer of computer science.",
        quiz=quiz,
        related_topics=["Computer Science", "Artificial Intelligence"]
    )
    # Save to history
    history.append({"id": len(history)+1, "url": req.url, "title": result.title})
    return result

# Get history endpoint
@app.get("/history")
def get_history():
    return history
