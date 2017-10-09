#! env bin/python
# codding = utf-8
from threading import Lock, Thread

l = Lock()  # выполняется весь поток сразу


def f1():
    l.acquire()
    for x in range(100):
        print(x)
    l.release()


t1 = Thread(target=f1())
t1.start()
t2 = Thread(target=f1())
t2.start()
t3 = Thread(target=f1())
t3.start()
