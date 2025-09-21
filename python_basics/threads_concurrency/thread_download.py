import threading
import requests # type: ignore
import time

def download_file(url, filename):
    print(f"{threading.current_thread().name} started downloading {filename}")
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"{threading.current_thread().name} finished downloading {filename}") 
    
    
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]
    
start = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=download_file, args=(url, f"img.{url.split('/')[-1]}"))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.time()

print(f"All downloads done in {end-start:.2f} second")
    
