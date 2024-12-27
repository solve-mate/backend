from fastapi import APIRouter
from pydantic import BaseModel
from app.chains.basic_chain import get_gpt_response

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/chatgpt")
async def ask_chatgpt(request: QuestionRequest):
    response = get_gpt_response(request.question)
    return {"response": response}
