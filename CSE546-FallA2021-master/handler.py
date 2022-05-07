import boto3
import base64
import subprocess
from PIL import Image
from io import BytesIO
from subprocess import check_output
import time
import re
from subprocess import check_output
from eval_face_recognition import face_recognition

BUCKET_NAME = "face-recognition-videos"
FOLDER_NAME = "videos"
dbclient = boto3.client(
    'dynamodb',
    region_name='us-east-1'
)


def face_recognition_handler(event, context):
    print("Came here")
    coded_image = event["body"]
    bytes_data_img = bytes(coded_image, 'utf-8')
    decoded_b64_image = base64.decodebytes(bytes_data_img)
    pillow_image = Image.open(BytesIO(decoded_b64_image))

    recognised_face = face_recognition(pillow_image)
    dbclient = boto3.client(
        'dynamodb',
        region_name='us-east-1'
    )
    db_data = dbclient.get_item(
        TableName="group11_students_table",
        Key={
            'name': {'S': recognised_face}
        }
    )
    name = db_data['Item']['name']['S']
    major = db_data['Item']['major']['S']
    year = db_data['Item']['year']['S']
    db_result = {
        "name": name,
        "major": major,
        "year": year
    }
    return db_result
