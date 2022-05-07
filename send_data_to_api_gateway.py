import base64
import PIL
from io import BytesIO
import time
import requests
import json
from constants import API_HEADER_ACCESS_KEY, URL


def send_images_to_lambda():
    start_time = time.time()
    image_file_name = 'test_img/ak_30.png'
    img_data = open(image_file_name, 'rb').read()
    data = base64.b64encode(img_data)
    img_as_str = str(data, "utf-8")
    response = (requests.post(URL, data=img_as_str, headers={
        "Content-Type": "image/png; charset=UTF-8", "X-API-Key": API_HEADER_ACCESS_KEY}))
    latency = time.time() - start_time
    db_data = json.loads(response.text)
    output = f'The 1 person recognized: {db_data["name"]}, {db_data["major"]}, {db_data["year"]}'
    print(output)
    print("Latency: {:.2f} seconds.".format(latency))


if __name__ == "__main__":
    send_images_to_lambda()
