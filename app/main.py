from fastapi import FastAPI
from app.routers import gpt

app = FastAPI()

# GPT 라우터 추가
app.include_router(gpt.router, prefix="/api", tags=["GPT"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
