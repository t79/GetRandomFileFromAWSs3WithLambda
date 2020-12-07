import boto3
#from random import choice

urlDomain = 'http://filearchive.t79.it.s3-website-eu-west-1.amazonaws.com/'
regionName = 'eu-west-1'
databaseTable = 'filearchivenames'


def lambda_handler(event, context):
    dynamoDBClient = boto3.client('dynamodb', region_name=regionName)

    try:
        response = dynamoDBClient.scan(TableName=databaseTable)

        list = response['Items']  # <--- Getting out all the entries from the database.
        randomFileName = list[0]['name']['S']  # <--- Getting the filename of the first entry.

        # randomObject = choice()
        # randomObject[]

    except Exception as e:
        raise e

    return {
        'statusCode': 301,
        'headers': {
            'Cache-Control': 'no-store, must-revalidate',
            'Vary': 'Cookie'
        },
        'location': urlDomain + randomFileName # <--- Adding the filename to the URL.
    }