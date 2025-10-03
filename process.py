from multiprocessing import Process
import os

def square():
    for i in range(100):
        i * i

if __name__ == '__main__':

    process = []
    process_count = os.cpu_count() # get number of CPU cores(process equal to number of cores)

    # create processes
    for i in range(process_count):
        p = Process(target=square)
        process.append(p)

    # start processes
    for p in process:
        p.start()

    # wait for all processes to finish
    for p in process:
        p.join()

    print("End main process")            

