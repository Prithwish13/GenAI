import threading

tea_stock = 0

def restock():
    global tea_stock
    for _ in range(100000):
        tea_stock += 1
        
threads  = [threading.Thread(target=restock) for _ in range(4)]

[t.start() for t in threads]
[t.join() for t in threads]



print(f"Tea stock: {tea_stock}")  # Expected: 400000, Actual: Less than
