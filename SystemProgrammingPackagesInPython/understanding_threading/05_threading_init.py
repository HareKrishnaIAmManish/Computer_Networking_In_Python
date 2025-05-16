import threading
def myTask():
    print("hello world{}".format(threading.current_thread))
    print("Hello World: {}".format(threading.current_thread()))
myFirstThread=threading.Thread(target=myTask)
myFirstThread.start()
