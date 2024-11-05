import boto3
 
dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')  # Replace with your region
 
try:
    response = dynamodb_client.list_tables()
    table_names = response['TableNames']
    print("DynamoDB Tables:")
    for table_name in table_names:
        print(table_name)
except Exception as e:
    print("Error listing tables:", e)