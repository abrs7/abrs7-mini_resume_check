import base64
from PIL import Image
from io import BytesIO
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rank_with_profile_photo():
    # Load image and encode it
    with open("tests/assets/profile_pic.jpg", "rb") as image_file:
        encoded_photo = base64.b64encode(image_file.read()).decode("utf-8")
    print(encoded_photo)
    payload = {
        "resume": "Experienced Python developer with cloud and backend skills.",
        "job_description": "Seeking a backend developer with Python and AWS experience.",
        "photo": encoded_photo
    }

    response = client.post("/rank", json=payload)
    assert response.status_code == 200
    data = response.json()
    print(response.status_code)
    print(response.json())


    assert "score" in data
    assert "feedback" in data
    #check if photo check exist in
    assert "photo_check" in data
    assert isinstance(data["photo_check"], str)
