import logging

logging.basicConfig(level=logging.INFO)

def divide(a, b):
    """ checks the ZeroDividionError and returns the result"""
    try :
        return a/b
    except ZeroDivisionError:
        logging.info("Cannot divide by zero")

print(divide(1,5))