from logger import logging

def add(x,y):
    logging.info('Addition operation is taking place')
    return (x+y)

logging.warning('the addition function is called')
print(add(3,4))