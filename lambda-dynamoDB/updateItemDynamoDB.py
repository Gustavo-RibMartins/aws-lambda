import json
import boto3

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('produto')
    
    table.update_item(
    Key={
        'id_produto': event['id_produto']
    },
    UpdateExpression='SET valor = :valor',
    ExpressionAttributeValues={
        ':valor': 3000
    }
    
    return 200
)
