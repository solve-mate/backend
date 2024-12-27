from fastapi import FastAPI
from app.routers import gpt, image_processing


app = FastAPI()

# GPT 라우터 추가
app.include_router(gpt.router, prefix="/api", tags=["GPT"])

# 이미지 처리 라우터 등록
app.include_router(image_processing.router, prefix="/api/images")


@app.get("/")
def read_root():
    return {"Hello": "World"}
