import threading
import time
num_threads=4
def thread_message(message):
    global num_threads
    num_threads-=1
    time.sleep(4) 
    print("message from thread %s\n"%message)
while num_threads>0:
    print("i am %s"%num_threads)
    threading.Thread(target=thread_message("I am the %s thread"%num_threads)).start()
    time.sleep(4) 