import time

start = time.perf_counter() #start timer

def doSomething():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('done sleeping..')

doSomething()   #end of timer

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
