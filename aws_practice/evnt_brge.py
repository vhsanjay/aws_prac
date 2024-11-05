import boto3

# Initialize the EventBridge client
eventbridge_client = boto3.client('events', region_name='us-east-1')

try:
    # List EventBridge event buses
    response = eventbridge_client.list_event_buses()
    print("EventBridge Event Buses:")
    
    # Loop through and print each event bus name
    for bus in response['EventBuses']:
        print("Name:", bus['Name'])

except Exception as e:
    # Print an error message if something goes wrong
    print("Error listing EventBridge event buses:", e)
