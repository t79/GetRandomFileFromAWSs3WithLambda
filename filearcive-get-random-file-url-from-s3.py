import json
import boto3

bucketName = "filearchive.t79.it"


def lambda_handler(event, context):
    s3Client = boto3.client('s3')

    try:
        objectsResponse = s3Client.list_objects(Bucket=bucketName)
        if 'Contents' not in objectsResponse:
            return {'statusCode': 404}

        fileNamesList = []                          # <--- List for holding the filenames.
        for object in objectsResponse["Contents"]:  # <--- Iterate through the items/files.
            fileNamesList.append(object["Key"])     # <--- Add filename to list.

    except Exception as e:
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! there are '
                           + str(len(fileNamesList)) + ' objects: '     # <--- The number of files found.
                           + " ".join(name for name in fileNamesList))  # <--- Adding the names for the files to the response.
    }