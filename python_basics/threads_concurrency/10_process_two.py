from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching Some numbers.....")
    
    total = 0
    for i in range(10 ** 8):
        total += i
    print(f"Total : {total}")
    
    
if __name__ == "__main__":
    start = time.time()

    processes = [Process(target=cpu_heavy) for _ in range(2)]

    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"Total time taken : {time.time() - start:.2f} seconds")