import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucketName = event['Records'][0]['s3']['bucket']['name']
    bucketObject = event['Records'][0]['s3']['object']['key']
    print(bucketName)
    print(bucketObject)

    response = s3.get_object(Bucket=bucketName, Key=bucketObject)
    print(response)
    data = response['Body'].read().decode('utf-8')
    print(data)
