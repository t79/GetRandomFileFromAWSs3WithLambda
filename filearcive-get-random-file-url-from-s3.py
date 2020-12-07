import json
import boto3
from random import choice  # <--- Importing method for selecting a random item in a list.

bucketName = "filearchive.t79.it"
urlDomain = "http://filearchive.t79.it.s3-website-eu-west-1.amazonaws.com/"  # <--- The domain in the URL.


def lambda_handler(event, context):
    s3Client = boto3.client('s3')

    try:
        objectsResponse = s3Client.list_objects(Bucket=bucketName)
        if 'Contents' not in objectsResponse:
            return {'statusCode': 404}

        fileNamesList = []
        for object in objectsResponse["Contents"]:
            fileNamesList.append(object["Key"])

        randomFileName = choice(fileNamesList)  # <--- Choosing randomly one name in the list.

    except Exception as e:
        raise e

    return {
        'statusCode': 200,
        'body': urlDomain + randomFileName  # <--- Setting the URL to the file in the response.
    }