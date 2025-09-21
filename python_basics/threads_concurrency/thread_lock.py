import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(50000):
        with lock: # here with lock we have implemented the thread safety
            counter += 1
            
threads = [threading.Thread(target=increment) for _ in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f"final counter : {counter}")
        
