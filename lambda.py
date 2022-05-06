import json
import boto3
import base64
import os
import time
from botocore.exceptions import ClientError
from subprocess import check_output
# import PIL
# from io import BytesIO
import base64

BUCKET_NAME = "face-recognition-videos"
FOLDER_NAME = "videos"
s3 = boto3.client('s3')
def store_image_to_s3(file_name, image_file):
    try:
        response = s3.upload_file(file_name, BUCKET_NAME, image_file)
        print("image_loaded")
    except ClientError as e:
        logging.error(e)


def decode_base64(coded_string):
    #decoded = base64.b64decode(coded_string)
    file_name = "/tmp/" + str(int(time.time()) + 1) + ".png"
    print("The filename with time is:" + file_name)
    base64Image = bytes(coded_string, 'utf-8')
    # base64Image = bytes(coded_string)
    with open(file_name, "wb") as fh:
        fh.write(base64.decodebytes(base64Image))
    # decoded = open(file_name, "wb")
    # decoded.write(base64.decodebytes(base64Image))
    # decoded.close()
    store_image_to_s3(file_name, file_name)
    print(os.listdir("/tmp/"))
    return file_name
    # data = {}
    # data['img'] = coded_string
    # im = PIL.Image.open(BytesIO(base64.b64decode(data['img'])))
    # print("Pillow Data: "+ im)


def lambda_handler(event, context):
    file_name = decode_base64(event['body'])
    print(event['body'])
    # recognisedFaceOutput = check_output(["python3", "-W ignore", "./eval_face_recognition.py", "--img_path", file_name]).strip().decode('utf-8')
    # print(recognisedFaceOutput)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Cloud Lambda! ' + file_name)
    }

    # unused code
    # with open(file_name, "w+") as fh:
    #   fh.write(base64.decodebytes(base64Image))
    # data_file = open(file_name, 'w+')
    # data_file.write(str(decoded))
    # data_file.close()