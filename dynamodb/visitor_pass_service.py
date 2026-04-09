from dynamodb.dynamo_client import (
    visitor_pass_table,
    history_table
)
import time

def create_visitor_pass(pass_id, visitor_name, issued_by):
    expires_at = int(time.time()) + 3600  # 60 mins TTL

    visitor_pass_table.put_item(
        Item={
            "passId": pass_id,
            "visitorName": visitor_name,
            "issuedBy": issued_by,
            "expiresAt": expires_at
        }
    )

def archive_pass(pass_item):
    history_table.put_item(Item=pass_item)
``