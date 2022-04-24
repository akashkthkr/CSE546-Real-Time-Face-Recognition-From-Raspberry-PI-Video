import json
BUCKET_NAME = "face-recognition-videos"
FOLDER_NAME = "videos"


def lambda_handler(event, context):
    print(event)
    base64_encoded_image = json.loads(event.body)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Cloud Lambda! ')
    }
