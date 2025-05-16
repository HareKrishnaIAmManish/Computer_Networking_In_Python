import threading
import time
def def_messgage(message):
    time.sleep(4)
    print("hii"+message)
# thread1=threading.Thread(target=def_messgage("user1")) #here what you are doing is calling the function immediately, instead of passing it as a target to the thread
# thread2=threading.Thread(target=def_messgage("user2"))
thread1 = threading.Thread(target=def_messgage, args=("user-1",))
thread2 = threading.Thread(target=def_messgage, args=("user-2",))
thread1.start()
thread2.start()

