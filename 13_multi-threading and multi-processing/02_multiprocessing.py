# Process that run in parallel
# CPU-bound task that are heavy on CPU usage(e.g, mathematical computations, data processing)
# Parallel execution - Multiple cores of the CPU


import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")
        
        
def cude_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cude: {i*i*i}")
        
        
# entry point
if __name__ =='__main__':
        
            ##  create 2 processes
            p1 = multiprocessing.Process(target=square_number)
            p2 = multiprocessing.Process(target=cude_number)


            t = time.time()
            ## start the process
            p1.start()
            p2.start()


            # wait for the process to complete
            p1.join()
            p2.join()

            stop_time = time.time()-t

            print(stop_time)