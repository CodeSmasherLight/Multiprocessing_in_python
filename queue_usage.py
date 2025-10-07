from multiprocessing import Process, Queue


def square(numbers, q):
    for n in numbers:
        q.put(n * n)

def make_negative(numbers, q):
    for n in numbers:
        q.put(-1 * n)


if __name__ == '__main__':
    
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()  

    p1.join()
    p2.join()
    
    # get data from the queue until it is empty
    while not q.empty():
        print(q.get())