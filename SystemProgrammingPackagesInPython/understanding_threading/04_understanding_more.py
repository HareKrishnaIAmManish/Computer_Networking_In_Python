import threading
import time
def task(name):
    # for i in range(3):
        # print(f"{name}: {i}")
        print(f"{name}")
        time.sleep(1)
thread1 = threading.Thread(target=task, args=("Thread-1",))
thread2 = threading.Thread(target=task, args=("Thread-2",))
thread1.start()
thread2.start()
