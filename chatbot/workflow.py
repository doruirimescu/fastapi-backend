# A workflow is a sequence of steps that the chatbot will follow to gather data.

from typing import List
from pydantic import BaseModel


class Question(BaseModel):
    field: str
    question: str


class Section(BaseModel):
    section: str
    questions: List[Question]
