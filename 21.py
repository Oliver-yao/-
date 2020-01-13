from multiprocessing import Process
import os


def info(title):
    print(title)
    print("module name:",__name__)
    # 得到父进程的 id
    print('parent process :', os.getppid())
    # 得到本身进程的 id
    print('process id:',os.getpid())

def f(name):
    info('function f')
    print('Hello ',name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f,args=('bob',))
    p.start()
   # p.join()