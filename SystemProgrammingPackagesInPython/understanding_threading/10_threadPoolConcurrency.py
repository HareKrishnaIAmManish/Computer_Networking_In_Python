from concurrent.futures import ThreadPoolExecutor
import threading
def view_thread():
    print("executing thread")
    print("accesing thread : {}".format(threading.get_ident()))
    print("thread excecuted {}".format(threading.current_thread()))
def main():
    executor=ThreadPoolExecutor(max_workers=3)
    thread1=executor.submit(view_thread)
    thread2=executor.submit(view_thread)
    thread3=executor.submit(view_thread)
if __name__=='__main__':
    main()    
