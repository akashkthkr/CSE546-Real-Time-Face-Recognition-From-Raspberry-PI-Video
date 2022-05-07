import boto3
import base64
from PIL import Image
from io import BytesIO
import json
from eval_face_recognition import face_recognition

dbclient = boto3.client(
    'dynamodb',
    region_name="us-east-1"
)


def face_recognition_handler(event, context):
    body = json.loads(event["body"])
    coded_image = body["imgBase64"]
    bytes_data_img = bytes(coded_image, 'utf-8')
    decoded_b64_image = base64.decodebytes(bytes_data_img)
    pillow_image = Image.open(BytesIO(decoded_b64_image))

    recognised_face = face_recognition(pillow_image)
    print(recognised_face)
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
