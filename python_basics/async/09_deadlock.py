import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        print("Task 1 acquired lock 1")
        with lock2:
            print("Task 1 acquired lock 2")
            print("Task 1 completed")
            
def task2():
    with lock2:
        print("Task 2 acquired lock 2")
        with lock1:
            print("Task 2 acquired lock 1")
            print("Task 2 completed")
            
            
threading.Thread(target=task1).start()
threading.Thread(target=task2).start()

# Deadlock occurs here because task1 holds lock1 and waits for lock2, while task2 holds lock2 and waits for lock1.

# Python profiling tools 1. /py-spy 2. vprof 3. cProfile