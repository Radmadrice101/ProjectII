"""
AuditLogs Table Access Layer

Stores INSERT / MODIFY / REMOVE events
for visitor passes using DynamoDB Streams + Lambda
"""

import boto3
from datetime import datetime, timezone
import json

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

AUDIT_LOGS_TABLE_NAME = "AuditsLogs"
audit_logs_table = dynamodb.Table(AUDIT_LOGS_TABLE_NAME)


def write_audit_log(
    pass_id: str,
    event_type: str,
    table_name: str,
    old_value: dict | None,
    new_value: dict | None,
):
    """
    Write an audit record.
    PassID is used as the partition key (required by table schema).
    """

    timestamp = datetime.now(timezone.utc).isoformat()

    item = {
        "PassID": pass_id,                 # ✅ REQUIRED PRIMARY KEY
        "eventType": event_type,           # INSERT / MODIFY / REMOVE
        "tableName": table_name,
        "timestamp": timestamp,
        "oldValue": json.dumps(old_value) if old_value else None,
        "newValue": json.dumps(new_value) if new_value else None,
    }

    audit_logs_table.put_item(Item=item)