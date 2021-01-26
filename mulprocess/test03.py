'''
 获取进程号pid 和获取进程的父进程ppid
'''
import os
import time
import multiprocessing

def sing(num):
    print("唱歌进程的pid：",os.getpid())
    print("唱歌进程父进程的pid：", os.getppid())
    for i in range(num):
        print("唱歌-----")
        time.sleep(0.5)

def dance(num):
    print("跳舞进程的pid：", os.getpid())
    print("跳舞进程父进程的pid：", os.getppid())
    for i in range(num):
        print("跳舞-----")
        time.sleep(0.5)

if __name__ == "__main__":
    sing_process = multiprocessing.Process(target=sing,args=(3,))
    dance_process = multiprocessing.Process(target=dance,kwargs={"num":3})
    sing_process.start()
    dance_process.start()