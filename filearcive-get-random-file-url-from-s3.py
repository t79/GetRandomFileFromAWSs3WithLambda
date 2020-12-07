import json
import boto3
from random import choice

bucketName = "filearchive.t79.it"
urlDomain = "http://filearchive.t79.it.s3-website-eu-west-1.amazonaws.com/"


def lambda_handler(event, context):
    s3Client = boto3.client('s3')

    try:
        objectsResponse = s3Client.list_objects(Bucket=bucketName)
        if 'Contents' not in objectsResponse:
            return {'statusCode': 404}

        fileNamesList = []
        for object in objectsResponse["Contents"]:
            fileNamesList.append(object["Key"])

        randomFileName = choice(fileNamesList)

    except Exception as e:
        raise e

    return {
        'statusCode': 301,  # <--- Changing the status code.
        'location': urlDomain + randomFileName  # <--- Changing to the key for that status.
    }