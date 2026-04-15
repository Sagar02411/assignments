# Q15 (Medium) – Logging + Best Practices
import logging

logger = logging.getLogger("SimpleLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)

def divide(a, b):
    try:
        result = a/b
        logger.info(f"result : {result}")
        return result
    except ZeroDivisionError:
        logger.error("Can not devide by zero")
    return a / b
print(divide(2,2))