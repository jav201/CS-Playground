# This is only one alternative for threading.
# There are far more referenced on the book "Python Programming by M. Lutz"
import threading

class Power:
    def __init__(self,i):
        self.i = i
    def action(self):
        print(self.i**2)

if __name__ == '__main__':
    obj = Power(2)
    threading.Thread(target = obj.action()).start()