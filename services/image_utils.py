from PIL import Image
import io
import pytesseract


async def process_image(file):
    # 파일을 Pillow 이미지로 변환
    if file.content_type not in ["image/png", "image/jpeg"]:
        raise ValueError("지원되지 않는 파일 형식입니다. PNG 또는 JPEG만 허용됩니다.")

    image = Image.open(io.BytesIO(await file.read()))
    return image


def extract_text_from_image(image):
    # Tesseract OCR을 사용해 텍스트 추출
    text = pytesseract.image_to_string(image)
    return text
