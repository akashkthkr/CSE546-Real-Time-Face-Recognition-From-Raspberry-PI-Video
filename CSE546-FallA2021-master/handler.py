import boto3
import base64
import subprocess
from PIL import Image
from io import BytesIO
from subprocess import check_output
import time
from subprocess import check_output

BUCKET_NAME = "face-recognition-videos"
FOLDER_NAME = "videos"
s3 = boto3.client('s3')


def store_image_to_s3(file_name, image_file):
    try:
        response = s3.upload_file(file_name, BUCKET_NAME, image_file)
        print("image_loaded")
    except Exception as e:
        print(e)


def store_image_in_tmp(image_data, img_file_name):
    with open(img_file_name, "wb") as fh:
        fh.write(base64.decodebytes(image_data))


def face_recognition_handler(event, context):
    print("Came here")
    img_file_name = "/tmp/" + str(int(time.time()) + 1) + ".png"
    coded_image = event["body"]
    decode_b64_image = base64.b64decode(coded_image)
    store_image_in_tmp(decode_b64_image, img_file_name)

    # Printing the base64 bytes to check if it is correctly converting
    eval_data = open(img_file_name, "rb").read()
    data_img_to_be_sent = base64.b64encode(eval_data).decode("utf-8")
    print(data_img_to_be_sent)

    recognised_face = check_output(
        ["python3", "-W ignore", "./eval_face_recognition.py", "--img_path", img_file_name]).strip().decode('utf-8')
    print("The output for this request is: " + str(recognised_face))
    response = {
        'statusCode': 200,
        'body': recognised_face
    }
    return response
