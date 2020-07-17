import threading
import time

class Cake:
    def __init__(self,ckid,cknm,ckprice):
        self.cakeId =ckid
        self.cakeName = cknm
        self.cakePrice = ckprice

    def __str__(self):
        return f"""
        Cake Id : {self.cakeId} Cake Name : {self.cakeName} Cake Price :{self.cakePrice}
        """

    def __repr__(self):
        return str(self)

import random

def counter():
    cnt = 0
    while True:
        cnt += 1
        yield cnt

gen =counter()

def generat_cake():
    time.sleep(1)
    cnt =next(gen)
    return Cake(ckid=cnt,cknm='Cheese Cake'+str(cnt),ckprice=random.randint(500,1000))

bakery = []
def producer_task():
    while True:
        cake = generat_cake()
        bakery.append(cake)
        time.sleep(1)
        print('\n'+threading.current_thread().name+ "--->",bakery)

def consumer_task():
    if not bakery: #if cakes are not available in bakery wait for 5 seconds and print message
        time.sleep(5)
        print('waiting for cakes to be available ---Initial')

    while bakery: #after 5 seconds
        if not bakery: # one more time check cakes in bakery
            time.sleep(5)
            print('waiting for cake to be available ---After')
        cake = bakery.pop(0) #consume first cake
        time.sleep(2)
        print('\n'+threading.current_thread().name, "--->", cake)

if __name__ == '__main__':
    t1 =threading.Thread(target=producer_task,name='Producer')
    t2 = threading.Thread(target=consumer_task,name='Consumer')
    t1.start()
    t2.start()