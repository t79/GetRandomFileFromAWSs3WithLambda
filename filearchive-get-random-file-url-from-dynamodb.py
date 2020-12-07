import boto3
from random import choice  # <--- Adding the method for getting a random entry in a list

urlDomain = 'http://filearchive.t79.it.s3-website-eu-west-1.amazonaws.com/'
regionName = 'eu-west-1'
databaseTable = 'filearchivenames'


def lambda_handler(event, context):
    dynamoDBClient = boto3.client('dynamodb', region_name=regionName)

    try:
        response = dynamoDBClient.scan(TableName=databaseTable)

        list = response['Items']
        randomFileName = ''
        if len(list):
            randomEntry = choice(list)                  # <--- Getting a random entry and its filename
            randomFileName = randomEntry['name']['S']   #

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