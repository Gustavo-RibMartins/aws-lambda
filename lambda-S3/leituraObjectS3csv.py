import boto3
import json

def lambda_handler(event, context):
    
    arquivo = 'DB-tmp-S3-Lambda-Produtos.csv'
    bucket = 'datalake-raw-layer-ingest'
    
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, arquivo)
    body = obj.get()['Body'].read().decode()
    print(body)
