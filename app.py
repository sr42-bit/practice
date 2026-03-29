import logging
from operator import add

logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    a = int(event.get("a", 0))
    b = int(event.get("b", 0))

    result = add(a, b)

    return {
        'statusCode': 200,
        'body': f'Result is {result}'
    }


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Serverless!'
    }