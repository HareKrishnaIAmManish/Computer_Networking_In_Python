import threading
class ThreadWorker(threading.Thread):
    #our workers constructer
    def __init__(self):
        super(ThreadWorker,self).__init__() # or super().__init__()
    def run(self):
        for i in range(10):
            print(i) 