#! env bin/python
# codding = utf-8
import threading
import time
sem = threading.Semaphore()


def fun1():
    while True:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.5)


def fun2():
    while True:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.1)


t = threading.Thread(target=fun1)
t.start()
t2 = threading.Thread(target=fun2)
t2.start()


'''from threading import Lock, Thread, Semaphore

l = Lock()  # выполняется весь поток сразу


def f1():
    l.acquire()
    for x in range(100):
        print(x)
    l.release()


t1 = Semaphore(target=f1())
t1.start()
t2 = Thread(target=f1())
t2.start()
t3 = Thread(target=f1())
t3.start()'''
