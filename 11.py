import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum, loopSum
    for i in range(1,loopSum):
        sum += 1

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1

if __name__ == '__main__':
    print("Starting ... {0}".format(sum))

    # 开始多线程的实例看执行结果是否一致
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    '''
    每次顺序执行的结果都一样
    myAdd()
    myMinu()
    '''
    print("Done...{0}".format(sum))