'''
    多进程
    主进程等待所有子进程结束在结束
'''
import time
import multiprocessing

def work():
    for i in range(10):
        print('进行中...')
        time.sleep(0.2)

if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=work)
    sub_process.start()
    time.sleep(1)
    print("主进程结束了...")
