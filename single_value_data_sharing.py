from multiprocessing import Process, Value, Lock
import time

def add_100(num, lock):
    for i in range(100):
        time.sleep(0.01)  # simulate some work
        with lock:
            num.value += 1  # increment the shared variable

if __name__ == '__main__':

    lock = Lock()
    # shared memory variable
    num = Value('i', 0)  # 'i' indicates a signed integer
    print("Initial Value:", num.value)  # should print 0

    p1 = Process(target=add_100, args=(num, lock))
    p2 = Process(target=add_100, args=(num, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final Value:", num.value)  # should print 200(without race condition), but without Lock it may not be 200 every time 

