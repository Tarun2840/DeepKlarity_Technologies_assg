# models.py
from pydantic import BaseModel
from typing import List, Optional


class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str
    explanation: Optional[str] = None
    difficulty: Optional[str] = "medium"


class QuizOutput(BaseModel):
    topic: str
    questions: List[QuizQuestion]


class QuizRequest(BaseModel):
    topic: str
