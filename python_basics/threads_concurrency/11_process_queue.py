from multiprocessing import Process, Queue
import time



def prepare_tea(queue):
    queue.put("Masala Tea is prepared")
    
    
if __name__ == "__main__":
    queue = Queue()

    p = Process(target=prepare_tea, args=(queue,))
    p.start()
    p.join()

    print(queue.get())