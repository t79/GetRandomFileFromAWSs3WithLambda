#import boto3
#from random import choice

urlDomain = "http://filearchive.t79.it.s3-website-eu-west-1.amazonaws.com/"

def lambda_handler(event, context):
    # Client = boto3.client()

    try:
        print('Ned something inside of try for just making this code to run!')
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