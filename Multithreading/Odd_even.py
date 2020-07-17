import threading

class Odd_Even:
    number = 0
    limit = 20
    odd_event = threading.Event()
    even_event = threading.Event()
    def print_odd(self):
        while Odd_Even.number <= Odd_Even.limit:
            Odd_Even.number += 1
            print(Odd_Even.number)
            Odd_Even.even_event.set()
            Odd_Even.odd_event.clear()
            Odd_Even.odd_event.wait()
        Odd_Even.even_event.wait()


    def print_even(self):
        # print('in print even method')
        Odd_Even.even_event.wait()
        while Odd_Even.number <= Odd_Even.limit:
            Odd_Even.number += 1
            print(Odd_Even.number)
            Odd_Even.odd_event.set()
            Odd_Even.even_event.clear()
            Odd_Even.even_event.wait()
        Odd_Even.odd_event.set()

if __name__ == '__main__':
    n1 = Odd_Even()
    no1 = threading.Thread(target = n1.print_odd)
    no2 = threading.Thread(target= n1.print_even)
    no1.start()
    no2.start()
    # no1.join()
    # no2.join()

