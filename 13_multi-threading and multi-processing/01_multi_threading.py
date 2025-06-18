# Multi-threading
# When to use Multithreading
# I/O-bound task: Task spend more time waiting for I/O operation (e.g file operation,network requests).
# Concurrent execution: When you want to improve the throughout of your application by performing multiple operation concurrently.


import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"number: {i}")
        
def print_character():
    for char in 'abcdef':
        time.sleep(2)
        print(f"character: {char}")
    
  
# create 2 threads
th1 = threading.Thread(target=print_numbers)
th2 = threading.Thread(target=print_character)
  
        
t = time.time()        
# print_numbers()
# print_character()

# start the thread
th1.start()
th2.start()

# wait for the thread to complete and join
th1.join()
th2.join()


stop_time = time.time()-t
print(stop_time)