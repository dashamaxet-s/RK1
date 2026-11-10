import threading

counter = 0
lock = threading.Lock()  

def worker() -> None:
    global counter
    for _ in range(100_000):
        with lock:       
            counter += 1

threads = [threading.Thread(target=worker) for _ in range(8)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(counter)