import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Replace with your region
table_name = 'dynamodb'  # Replace with your DynamoDB table name
table = dynamodb.Table(table_name)
item = {
    'name': 'john',  # Replace with your actual primary key
    'age': '15'
}
try:
    table.put_item(Item=item)
    print(f"Item added to table '{table_name}':")
    print(item)
except Exception as e:
    print("Error adding item:", e)

 