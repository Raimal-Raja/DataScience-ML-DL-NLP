import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M: %S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
        
        ]
    )

logger = logging.getLogger('ArithmeticApp')


def add(a,b):
    
    logger.debug('Adding two numbers')
    return a+b

def subtract(a,b):
    logger.debug(f"Subtracting {b} from {a}")
    return a-b

def multiply(a,b):
    logger.debug('Multiplying two numbers')
    result = a*b
    return result
def division(a,b):
    try:
        result = a/b
        logger.debug(f'Dividing {b} from {a}')
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    

print(add(33,44))
print(subtract(33,44))
print(multiply(33,44))
print(division(33,44))
