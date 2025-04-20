import base64

b_encode = None
try:
    with open("assets/profile_pic.jpg", "rb") as img:
        b64 = base64.b64encode(img.read()).decode("utf-8")
    with open("result_byte.txt", "w") as result:
        result.write(b64)     
except Exception as e:
    print(f"Error occured due ****** {e}")        

   