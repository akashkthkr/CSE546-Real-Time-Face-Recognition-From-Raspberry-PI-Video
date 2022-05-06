import base64
import PIL
from io import BytesIO
import time



import requests
from constants import API_HEADER_ACCESS_KEY
# URL = "https://0x9zuskaok.execute-api.us-east-1.amazonaws.com/default/face-recog-eval"
URL = "https://16aw5l4jb7.execute-api.us-east-1.amazonaws.com/default/face-recog-eval"
# HTTP call URL Below one

# def check_pillow(coded_string):
#     data = {}
#     data['img'] = coded_string
#     im = PIL.Image.open(BytesIO(base64.b64decode(data['img'])))
#     print("Pillow Data: " + str(im))
#     return im


# def post_video_to_aws_api_gateway():
#     result = "Alpha"
#     beta = "Beta"
#     img_and_result = f"({beta}, {result})"
#     print(f"Image and its recognition result is: {img_and_result}")
#     files = {'file': open('test_img.png', 'rb')}
#     value = base64.b64encode(files['file'].read())
#     strValue = str(value, 'utf-8')
#     ans = check_pillow(strValue)
#     print(ans)
#     # imgDataObj = {'image': strValue}
#     # response = requests.post(URL, files=value,  headers={"Content-Type": "image/png", "X-API-Key": API_HEADER_ACCESS_KEY})
#     # response = requests.post(URL, data=strValue,  headers={
#     #     "Content-Type": "text/html; charset=UTF-8", "X-API-Key": API_HEADER_ACCESS_KEY})
#     # print(response)
#     # print(response.json())

def send_images_to_lambda():
    start_time = time.time()
    img_data = open('test_img.png', 'rb').read()
    data = base64.b64encode(img_data).decode("utf-8")
    print(data)
    response = (requests.post(URL, data=data, headers={
        "Content-Type": "image/png; charset=UTF-8", "X-API-Key": API_HEADER_ACCESS_KEY}))
    latency = time.time() - start_time
    print("Latency: {:.2f} seconds.".format(latency))
    print(response.json())

if __name__ == "__main__":
    # post_video_to_aws_api_gateway()
    send_images_to_lambda()
