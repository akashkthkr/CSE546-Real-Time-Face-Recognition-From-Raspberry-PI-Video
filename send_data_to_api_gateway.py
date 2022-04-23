import requests
API_HEADER_ACCESS_KEY = "0K3vXKxiE53WVGEtDLGmQ5X3TC1cS7c19CCofaC8"
URL = "https://z6itiyatih.execute-api.us-east-1.amazonaws.com/production/test1"


def post_video_to_aws_api_gateway():
    files = {'file': open('test.jpeg', 'rb')}
    response = requests.post(URL, files=files,  headers={
                             "Content-Type": "image/png", "X-API-Key": API_HEADER_ACCESS_KEY})
    print(response)


if __name__ == "__main__":
    post_video_to_aws_api_gateway()
