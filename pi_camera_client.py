from picamera import PiCamera
import time
import multiprocessing
import boto3
from botocore.exceptions import ClientError
import os
import requests
import constants
import logging
from PIL import Image

# API_HEADER_ACCESS_KEY = "0K3vXKxiE53WVGEtDLGmQ5X3TC1cS7c19CCofaC8"
# URL = "https://z6itiyatih.execute-api.us-east-1.amazonaws.com/production/test1"

s3_client = boto3.client('s3',
                         region_name=constants.REGION_NAME, aws_access_key_id=constants.AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=constants.AWS_ACCESS_KEY_SECRET)


def post_video_to_s3(video_name):
    bucket_name = constants.AWS_S3_BUCKET_NAME
    try:
        response = s3_client.upload_file(video_name, bucket_name, video_name)
        print("image_loaded")
    except ClientError as e:
        logging.error(e)

def send_frame_to_lambda(video_name):
    path = "/tmp/"
    video_file_path = "./"
    os.system("ffmpeg -i " + str(video_file_path) + video_name + " -r 1 " + str(path) + "image-%3d.jpeg")


def capture_video():
    camera = PiCamera()
    camera.resolution = (160, 160)
    camera.vflip = True
    camera.start_preview()
    time.sleep(2)

    for i in range(2):
        video_name = "video" + str(i) + ".h264"
        image_name = "image" + str(i)

        #record video and capture image at 0.3s
        camera.start_recording(video_name)
        camera.wait_recording(0.3)
        camera.capture(image_name + '.data', 'rgb', use_video_port=True)
        camera.wait_recording(0.2)
        camera.stop_recording()

        #convert to png
        rawData = open(image_name + '.data', 'rb').read()
        imgSize = (160, 160)  # the image size
        img = Image.frombytes('RGB', imgSize, rawData)
        img.save(image_name + '.png')

        # creating processes
        p1 = multiprocessing.Process(target=post_video_to_s3, args=(video_name, ))
        p2 = multiprocessing.Process(target=send_frame_to_lambda, args=(video_name, ))

        # starting processes
        p1.start()
        p2.start()

        # wait until processes are finished
        p1.join()
        p2.join()


if __name__ == "__main__":
    capture_video()
