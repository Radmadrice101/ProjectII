import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

visitor_table = dynamodb.Table("Visitors_pass")
history_table = dynamodb.Table("History_Visitors_pass")

PASS_ID = "PASS#FINAL001"

# Get the item from Visitors_pass
response = visitor_table.get_item(
    Key={"PassID": PASS_ID}
)

item = response.get("Item")

if not item:
    print("No item found to archive.")
    exit(0)

# Put item into History_Visitors_pass
history_table.put_item(Item=item)

# Delete item from Visitors_pass
visitor_table.delete_item(
    Key={"PassID": PASS_ID}
)

print("✅ Pass archived successfully:")
print(item)
