import boto3

regionName = 'eu-west-1'
databaseTable = 'filearchivenames'


def lambda_handler(event, context):
    dynamoDBClient = boto3.client('dynamodb', region_name=regionName)

    try:
        dynamoDBClient.put_item(TableName=databaseTable,
                Item={'name': {'S': event['Records'][0]['s3']['object']['key']}})  # <--- Adding the filename from S3 to the database.

    except Exception as e:
        raise e