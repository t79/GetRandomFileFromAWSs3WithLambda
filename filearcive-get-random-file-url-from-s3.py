import json
import boto3 # <--- Importing the AWS python library

def lambda_handler(event, context):
    s3Client = boto3.client('s3') # <--- Create a low-level S3 client

    try:                                            #
        bucketResponse = s3Client.list_buckets()    # <--- Trying to read from the S3 bucket
    except Exception as e:                          #
        raise e                                     #

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! there are '
                           + str(len(bucketResponse["Buckets"])) + ' bukets') # <--- Adding number of buckets in the return statement.
    }