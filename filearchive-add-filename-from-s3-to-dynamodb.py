# -- The code we keep from the get function.
# -- And adding entry to database.
import boto3

regionName = 'eu-west-1'
databaseTable = 'filearchivenames'


def lambda_handler(event, context):
    dynamoDBClient = boto3.client('dynamodb', region_name=regionName)

    try:
        dynamoDBClient.put_item(TableName=databaseTable, Item={'name': {'S': 'blueocean.jpg'}})  # <--- Adding entry to the database.
    except Exception as e:
        raise e