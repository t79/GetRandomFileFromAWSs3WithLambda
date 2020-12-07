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

        objects = objectsResponse['Contents']   # <--- Alternativ way for getting the filename
        randomObject = choice(objects)          #
        randomFileName = randomObject['Key']    #

    except Exception as e:
        raise e

    return {
        'statusCode': 301,
        'headers': {
            'Cache-Control': 'no-store, must-revalidate',
            'Vary': 'Cookie'
        },
        'location': urlDomain + randomFileName
    }