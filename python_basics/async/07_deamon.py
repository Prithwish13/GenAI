import threading
import time

def monitor_temperature():
    while True:
        time.sleep(1)
        print("Monitoring temperature...")

# threading.Thread(target=monitor_temperature, daemon=True).start() # if daemon=True, the thread will exit when the main program exits
threading.Thread(target=monitor_temperature).start() # if daemon=False, the thread will keep running even after the main program exits

print("Main program is running...")
time.sleep(5)
print("Main program is exiting...")

# run. the code using profiling
# "python -m cProfile -s time 07_deamon.py"