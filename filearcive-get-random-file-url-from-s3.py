import json
import boto3

bucketName = "filearchive.t79.it"  # <--- Specifing the name of the S3 bucket.

def lambda_handler(event, context):
    s3Client = boto3.client('s3')

    try:
        objectsResponse = s3Client.list_objects(Bucket=bucketName)  # <--- Changes from getting the buckets to get the files in one specific bucket.
        if 'Contents' not in objectsResponse:                       # <--- Checking that bucket are not empty
            return {'statusCode': 404}                              #

        print(objectsResponse)

    except Exception as e:
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! there are '
                           + str(len(objectsResponse['Contents'])) + ' objects') # <--- Changing from number of buckets to number of files.
    }