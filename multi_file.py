from multiprocessing import Pool
import time
import threading
import time
from threading import Lock, Thread


l = Lock()  # выполняется весь поток сразу

def file(x):
    #time.sleep(60)
    l.acquire()

    name = str(x)+'.txt'
    f = open(name, 'w')
    lst = range(50)
    for index in lst:
        f.write(str(index))
    l.release()
        #return x*x


if __name__ == '__main__':
    count = input('count =')
    count1 = input('count1 = ')
    for i in range(int(count)):
        t = 't' + str(i)
        t = threading.Thread(target=file(i))
        t.start()


'''if __name__ == '__main__':
    count = input('count =')
    count1 = input('count1 = ')
    #f = open('text.txt', 'w')
    with Pool(count) as p:
        file(p)
        #print(p.map(f, [1, 2, 3]))'''