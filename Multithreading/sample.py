import threading
import time

one_to_ten = threading.Event()
hundredone_to__hundreadten = threading.Event()


def func1():
    for item in range(1,11):
        print(item)
        # time.sleep(1)
        hundredone_to__hundreadten.set()
        one_to_ten.clear()
        one_to_ten.wait()
    hundredone_to__hundreadten.set()
    print('Fun1 Completed')

def func2():
    hundredone_to__hundreadten.wait()
    for item in range(101,111):
        print(item)
        # time.sleep(1)
        one_to_ten.set()
        hundredone_to__hundreadten.clear()
        hundredone_to__hundreadten.wait()
    one_to_ten.set()
    print('Fun2 Completed')

if __name__ == '__main__':
    print('inside main function')
    t1 = threading.Thread(target=func1) #thread(worker)
    t2 = threading.Thread(target=func2) #thread(worker)
    t1.start()
    t2.start()
    # t1.join()
    t2.join()
      # wait for t1 to get completed
    print('main function completed') # main completed after t1