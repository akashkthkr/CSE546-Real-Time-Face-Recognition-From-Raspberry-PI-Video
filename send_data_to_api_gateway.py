import base64
import PIL
from io import BytesIO
import time
import requests


from constants import API_HEADER_ACCESS_KEY
URL = "https://wu9xll4did.execute-api.us-east-1.amazonaws.com/default/x86-face-recog"


def send_images_to_lambda():
    start_time = time.time()
    image_file_name = 'test_img/ab_12.png'
    img_data = open(image_file_name, 'rb').read()
    data = base64.b64encode(img_data).decode("utf-8")
    response = (requests.post(URL, data=data, headers={
        "Content-Type": "image/png; charset=UTF-8", "X-API-Key": API_HEADER_ACCESS_KEY}))
    latency = time.time() - start_time
    print("Latency: {:.2f} seconds.".format(latency))
    print(response.text)


if __name__ == "__main__":
    send_images_to_lambda()
