from PIL import Image
import base64
from io import BytesIO

def check_photo(photo_base64: str) -> dict:
    try:
        image_bytes = base64.b64decode(photo_base64)
        image = Image.open(BytesIO(image_bytes))
        image.verify()  # optional: check image validity

        # 🧪 Mock logic for now
        return {"photo_check": "Looks professional"}
    except Exception as e:
        print("🚫 Failed to analyze photo:", e)
        return {"photo_check": "Could not analyze photo"}