'''
Real-world example: multiprocessing for CPU-bound tasks
Scenario: Factorial calculation
Factorial calculations, especially for large numbers,
involve significant computational work, multiprocessing
can be used to distibute the workload across multiple
CPU cores, improving performance
'''

import multiprocessing
import math
import multiprocessing.pool
import sys
import time


# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(1000000)

# function to computer factorials of a given number

def compute_factorial(number):
    print(f"computing factorial of {number}")
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__ == '__main__':
    number = [123232, 24232,3535,45454]
    
    start_time = time.time()
    
    
    ## create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, number)
        
    end_time = time.time()
    
    print(f'Result: {results}')
    print(f'time taken: {end_time - start_time} seconds')