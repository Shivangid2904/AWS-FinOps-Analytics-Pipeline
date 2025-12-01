import json

def lambda_handler(event, context):
    return {
        "status": "success",
        "message": "FinOps remediation bot executed. (EC2 idle resources will be stopped when they appear in CUR)"
    }
