import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('produto')
    
    table.delete_item(
    Key={
        'id_produto': 5
    }
)
