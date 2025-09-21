import threading
import time

def take_order():
    for i in range(1, 4):
        print(f"taking order for #{i}")
        time.sleep(1)
        
def brew_tea():
    for i in range(1, 4):
        print(f"brewing tea for #{i}")
        time.sleep(2)
        
        
# Creating Threads

order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_tea)


order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All order has taken and tea brewed")