from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from services.image_utils import process_image, extract_text_from_image
import httpx  # HTTP 요청 라이브러리

router = APIRouter()

GPT_ENDPOINT = (
    "http://localhost:8000/api/chatgpt"  # GPT 엔드포인트 (변경 필요 시 수정)
)


@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # 1. 이미지 처리
        processed_image = await process_image(file)

        # 2. 이미지에서 텍스트 추출
        extracted_text = extract_text_from_image(processed_image)
        

        # 3. GPT에게 텍스트 전송 및 응답 받기
        async with httpx.AsyncClient() as client:
            gpt_request_payload = {"question": extracted_text}
            print("🚀 디버깅 중 🚀")
            gpt_response = await client.post(GPT_ENDPOINT, json=gpt_request_payload)
            print("🚀 디버깅 중 🚀")
        # GPT 응답 확인
        if gpt_response.status_code != 200:
            return JSONResponse(
                content={"error": "GPT 응답 실패", "details": gpt_response.text},
                status_code=gpt_response.status_code,
            )

        gpt_response_data = gpt_response.json()

        # 4. 결과 반환
        return {
            "message": "이미지 업로드 및 텍스트 추출, GPT 처리 완료",
            "extracted_text": extracted_text,
            "gpt_response": gpt_response_data.get("response"),
        }
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
