from multiprocessing import Process, Value
import time

def increment(counter):
    for _ in range(3):
        with counter.get_lock(): 
            counter.value += 1
    

if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    
    print("Finished Computing", counter.value)
