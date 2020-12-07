import boto3  # <--- Adding the AWS python library
#from random import choice

urlDomain = 'http://filearchive.t79.it.s3-website-eu-west-1.amazonaws.com/'
regionName = 'eu-west-1'                # <--- Adding position and name for the database.
databaseTable = 'filearchivenames'      #


def lambda_handler(event, context):
    dynamoDBClient = boto3.client('dynamodb',region_name=regionName)  # <--- Creating a low-level DynamoDB client.

    try:
        response = dynamoDBClient.scan(TableName=databaseTable)  # <--- Getting the content of the database.

        print(response)  # <--- Printing out the database response.
        # randomObject = choice()
        # randomFileName = randomObject[]

    except Exception as e:
        raise e

    return {
        'statusCode': 301,
        'headers': {
            'Cache-Control': 'no-store, must-revalidate',
            'Vary': 'Cookie'
        },
        'location': urlDomain  # + randomFileName
    }