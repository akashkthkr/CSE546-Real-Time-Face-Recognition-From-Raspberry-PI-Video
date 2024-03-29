import base64
import time
import requests
import subprocess
import boto3
from botocore.exceptions import ClientError
import logging
import json
import threading
from constants import AWS_S3_BUCKET_NAME, URL, REGION_NAME, AWS_ACCESS_KEY_SECRET, AWS_ACCESS_KEY_ID, API_HEADER_ACCESS_KEY


s3_client = boto3.client('s3',
                         region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_ACCESS_KEY_SECRET)


def recognize_face(data, start_time, i):
    res = requests.post(URL, json=data)
    latency = time.time() - start_time
    db_data = json.loads(res.text)
    output = f"The {i} person recognized: {db_data['name']}, {db_data['major']}, {db_data['year']}"
    print(output)
    print("Latency: {:.2f} seconds.".format(latency))


def post_video_to_s3(vid_name):
    try:
        response = s3_client.upload_file(vid_name, AWS_S3_BUCKET_NAME, vid_name)
    except ClientError as e:
        logging.error(e)


def sending_frames_and_videos_to_lambdas():
    lambda_threads = list()
    s3_threads = list()
    for i in range(600):
        # command first called
        video_file_from_pi = f"/home/pi/Desktop/raspi-client/videos/video-{i}.h264"
        command1 = f"raspivid -hf -w 160 -h 160 -fps 30 -o {video_file_from_pi} -t 500"
        subprocess.call(command1, shell=True)

        # command second called
        frames_from_pi = f"/home/pi/Desktop/raspi-client/frames/image-{i}.png"
        command2 = f'ffmpeg -hide_banner -loglevel error -i {video_file_from_pi} -vf "select=eq(n\,8)" -vframes 1  {frames_from_pi}'
        subprocess.call(command2, shell=True)

        with open(frames_from_pi, "rb") as img_file:
            img_bytes = base64.b64encode(img_file.read())
        img_as_str = str(img_bytes, 'utf-8')
        data = {
            "imgBase64": img_as_str
        }
        start_time = time.time()
        aws_lambda_thread = threading.Thread(target=recognize_face, args=(data, start_time, i + 1,))
        lambda_threads.append(aws_lambda_thread)
        aws_lambda_thread.start()

        aws_s3_thread = threading.Thread(target=post_video_to_s3, args=(video_file_from_pi,))
        s3_threads.append(aws_s3_thread)
        aws_s3_thread.start()

    for thread in lambda_threads:
        thread.join()
    for thread in s3_threads:
        thread.join()


def send_images_to_lambda():
    start_time = time.time()
    image_file_name = 'test_img/ak_7.png'
    img_data = open(image_file_name, 'rb').read()
    data = base64.b64encode(img_data).decode("utf-8")
    sent_data = {
        "imgBase64": data
    }
    response = (requests.post(URL, json=sent_data))
    latency = time.time() - start_time
    db_data = json.loads(response.text)
    output = f'The 1 person recognized: {db_data["name"]}, {db_data["major"]}, {db_data["year"]}'
    print(output)
    print("Latency: {:.2f} seconds.".format(latency))


if __name__ == "__main__":
    send_images_to_lambda()
    # sending_frames_and_videos_to_lambdas()
