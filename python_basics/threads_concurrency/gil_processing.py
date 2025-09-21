from multiprocessing import Process
import time

def crunch_numbers():
    print(f"Process started")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Process ended")
    
if __name__ == "__main__":
    start = time.time()
    
    p1 = Process(target=crunch_numbers)
    p2 = Process(target=crunch_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()


    print(f"total time taken {end - start:.2f} second")


