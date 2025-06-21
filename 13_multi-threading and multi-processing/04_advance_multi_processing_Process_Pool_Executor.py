from concurrent.futures import ProcessPoolExecutor
import time

def sqaure_number(number):
    time.sleep(1)
    return f'number: {number*number}'


numbers = [1,2,3,4,5,6]

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as exceutor:
        results  = exceutor.map(sqaure_number, numbers)
        
    for result in results:
        print(result) 