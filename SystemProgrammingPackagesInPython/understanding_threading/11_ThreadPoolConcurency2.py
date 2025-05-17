from concurrent.futures import ThreadPoolExecutor
# print(help(ThreadPoolExecutor.submit))
def message(message):
    print("processing {}".format(message))
def main():
    print("starting threadpoolexecutor")
    with ThreadPoolExecutor(max_workers=2) as executor:
        future=executor.submit(message,('message 1'))
        future=executor.submit(message,('message 2'))
    print("all task complete")
if __name__=='__main__':
    main()
    