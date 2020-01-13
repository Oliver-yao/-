import threading
import time

# 参数定义了最多几个线程同时使用资源
semphore = threading.Semaphore(3)

def func():
    if semphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + ' get semphore\n')
        time.sleep(15)
        semphore.release()
        print(threading.currentThread().getName() + " release semphore\n")

for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()