from PIL import Image
import base64
from io import BytesIO

def check_photo(photo_base64: str) -> dict:
    try:
        image_bytes = base64.b64decode(photo_base64)
        image = Image.open(BytesIO(image_bytes))
        image.verify()

        width, height = image.size
        format = image.format
        if format not in ["JPEG", "PNG"]:
            return {"photo_check": "Unsupported image format"}

        if width < 300 or height < 300:
            return {"photo_check": "Photo is too small"}

        if width > 3000 or height > 3000:
            return {"photo_check": "Photo is too large"}

        return {"photo_check": "Looks professional"}
    except Exception as e:
        print("🚫 Failed to analyze photo:", e)
        return {"photo_check": "Could not analyze photo"}