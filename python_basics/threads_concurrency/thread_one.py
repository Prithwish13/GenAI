import threading
import time

def prepare_tea(type_, wait_time):
    print(f"{type_} tea is brewing......")
    time.sleep(wait_time)
    print(f"{type_} is prepared")
    
t1 = threading.Thread(target=prepare_tea, args=('Ginger', 5))
t2 = threading.Thread(target=prepare_tea, args=('Black', 2))


start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"total time taken {end - start:.2f} second")