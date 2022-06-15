import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('produto')
    
    table.put_item(
    Item={
        'id_produto': event['id_produto'],
        'nome_produto': event['nome_produto'],
        'categoria': event['categoria'],
        'valor': event['valor']
    }
)