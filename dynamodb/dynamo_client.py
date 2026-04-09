import boto3

REGION = "us-east-1"

dynamodb = boto3.resource("dynamodb", region_name=REGION)

visitor_pass_table = dynamodb.Table("Visitors_pass")
history_table = dynamodb.Table("History_Visitors_pass")
audit_log_table = dynamodb.Table("AuditLog")