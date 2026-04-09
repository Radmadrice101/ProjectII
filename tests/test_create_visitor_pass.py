import time
import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"
)

table = dynamodb.Table("Visitors_pass")

response = table.put_item(
    Item={
        "PassID": "PASS#FINAL001",          # ✅ EXACT KEY NAME
        "visitorName": "Final Test User",
        "issuedBy": "Security",
        "expiresAt": int(time.time()) + 300
    }
)

print("SUCCESS:", response["ResponseMetadata"]["HTTPStatusCode"])