import base64
import PIL
from io import BytesIO
import time



import requests
from constants import API_HEADER_ACCESS_KEY
# URL = "https://0x9zuskaok.execute-api.us-east-1.amazonaws.com/default/face-recog-eval"
# URL = "https://16aw5l4jb7.execute-api.us-east-1.amazonaws.com/default/face-recog-eval"
URL = "https://wu9xll4did.execute-api.us-east-1.amazonaws.com/default/x86-face-recog"


def send_images_to_lambda():
    start_time = time.time()
    image_file_name = 'test_img/test_img1.png'
    img_data = open(image_file_name, 'rb').read()
    data = base64.b64encode(img_data).decode("utf-8")
    # name_and_data = [data, image_file_name]
    print(data)
    response = (requests.post(URL, data=data, headers={
        "Content-Type": "image/png; charset=UTF-8", "X-API-Key": API_HEADER_ACCESS_KEY}))
    latency = time.time() - start_time
    print("Latency: {:.2f} seconds.".format(latency))
    print(response.json())

if __name__ == "__main__":
    send_images_to_lambda()
