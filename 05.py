# 利用 time 函数，生成两个函数
# 顺序调用
# 计算总的运行时间
# 练习带参数的多线程启动方法
import time
# 导入多线程包
import threading

def loop1(in1):
    # ctime 得到当前时间
    print("Start loop 1 at :",time.ctime())
    # 把参数打印出来
    print("我是参数 ",in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("End loop 1 at:",time.ctime())


def loop2(in1, in2):
    # ctime 得到当前时间
    print("Start loop 2 at :",time.ctime())
    # 把参数 in1 和 in2  打印出来代表使用
    print("我是参数 ", in1, "和参数 ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at:",time.ctime())

def main():
    print("Starting at:",time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 生成 threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("shen",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("meng","yao",))
    t2.start()

    t1.join()
    t2.join()

    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()
