from multiprocessing import Process
import time

start = time.perf_counter() #start timer

def doSomething(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('done sleeping..')
'''
p1 = multiprocessing.Process(target=doSomething)
p2 = multiprocessing.Process(target=doSomething)

p1.start()
p2.start()

p1.join()
p2.join()
'''
Processes = []

if __name__ == '__main__':
    for _ in range(10):
        p = Process(target=doSomething, args=[1.5])
        p.start()
        Processes.append(p)

for process in Processes:
    process.join()


finish1 = time.perf_counter()

print(f'Finished in {round(finish1-start,2)} second(s)')
