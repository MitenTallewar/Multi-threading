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


bakery = []

def generat_cake():
    time.sleep(2)
    cnt =next(gen)
    return Cake(ckid=cnt,cknm='Cheese Cake'+str(cnt),ckprice=random.randint(500,1000))


def main_task():
    while True:
        print("------------------ ")
        if len(bakery) < 10:
            for item in range(10):
                cake =generat_cake()
                bakery.append(cake)
                time.sleep(1)
                print("Producer-->",bakery) 
        else:
            print("-------------------")
            for item in range(10):
                cake = bakery.pop(0)
                time.sleep(1)
                print("Consumer-->",bakery )
                print("Consume by shop--->",cake)
 
if __name__ == '__main__':
    t1 = threading.Thread(target=main_task)
    # t2 =  threading.Thread(target=consumer_task,name="Consumer")
    t1.start()
    # t2.start()