from multiprocessing import Process
import time

def brew_tea(name):
    print(f"Start brewing {name} tea")
    time.sleep(3)
    print(f"Finished brewing {name} tea")
    
    
if __name__ == "__main__": # ensure that the code inside this block only runs when the script is executed directly
    tea_makers = [
        Process(target=brew_tea, args=(f"type {i+1}", )) # ("type 1",) This is a tuple containing one string
        for i in range(3)
    ]
    
    
    # Start All Process
    for p in tea_makers:
        p.start()
        
    # Wait for all to complete
    
    for p in tea_makers:
        p.join()