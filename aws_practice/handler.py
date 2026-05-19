import json
from request_process.main import process_request
 
def lambda_handler(event, _):
    response = process_request(event)
    return {
        "statusCode": response.get("statusCode", 200),
        "body": json.dumps(response.get("body"))
    }

event ={
    "s3_File_Name" : "test.csv",
    }

response = process_request(event)
print(f"response{response}")