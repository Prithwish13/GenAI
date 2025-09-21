# GIL (Global Interpreter Lock) is used to avoid race around condition

import threading
import time

def brew_tea():
    print(f"{threading.current_thread().name} started the brewing process")
    count = 0
    for _ in range(50000000):
        count += 1
    print(f"{threading.current_thread().name} finished the brewing process")
    


t1 = threading.Thread(target=brew_tea, name="Tea-Maker-1")
t2 = threading.Thread(target=brew_tea, name="Tea-Maker-2")

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"Total time taken {end - start:.2f} seconds")