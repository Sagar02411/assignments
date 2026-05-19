import logging
from request_process.main import Process

logger = logging.getLogger("SimpleLogger")
logger.setLevel('INFO')

def lambda_handler(event, context):
    try:
        p = Process(event)
        p.run()
        return {
            "status code": 200,
            "message": "function completed"
        }    
    except Exception as e:
        logger.error(f"error in lambda handler: {str(e)}")
        
        return {"statusCode": 400,
                "message": str(e)}

context = ''

event = {"file": "xyz.csv"}

lambda_handler(event, context)