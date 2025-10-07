from multiprocessing import Pool


def cube(num):
    return num * num * num

if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    # map, apply, close, join(imp methods)
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0]) # apply is used for single argument execution by function
    
    pool.close() # always use close() before join()
    pool.join()
    
    print(result)
