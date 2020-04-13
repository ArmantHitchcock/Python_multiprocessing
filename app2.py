import concurrent.futures
import time

start = time.perf_counter()


def doSomething(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'
'''
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(doSomething, 1)
        f2 = executor.submit(doSomething, 1)
        print(f1.result())
        print(f2.result())
'''
'''
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(doSomething, 1) for _ in range(10)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
'''
'''
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(doSomething, sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
'''
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(doSomething, secs)
        #for result in results:
        #    print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
