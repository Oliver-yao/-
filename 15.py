import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def Func_1():
    print("func_1 starting...")
    lock_1.acquire(timeout=4)
    print("func_1 申请了 lock_1")
    time.sleep(2)
    print("func_1 等待 lock_2")
    rst = lock_2.acquire(timeout=2)
    if rst:
        print("func_1 已经得到 lock_2")
        lock_2.release()
        print("func_1 已经释放了 lock_2")
    else:
        print("func_1 申请不到 lock_2")
    lock_1.release()
    print("func_1 释放了 lock_1")

    print("func_1 Done...")


def Func_2():
    print("func_2 starting...")
    lock_2.acquire()
    print("func_2 申请了 lock_2")
    time.sleep(4)
    print("func_2 等待 lock_2")
    lock_1.acquire()
    print("func_2 申请了 lock_1")

    lock_1.release()
    print("func_2 释放了 lock_1")

    lock_2.release()
    print("func_2 释放了 lock_2")

    print("func_2 Done...")

if __name__ == '__main__':
    print("主程序启动。。。")
    t1 = threading.Thread(target=Func_1, args=())
    t2 = threading.Thread(target=Func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束")