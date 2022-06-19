# This is only one alternative for threading.
# There are far more referenced on the book "Python Programming by M. Lutz"
import threading, time

count = 0
def adder(addblock):
    global count
    with addblock:
        count += 1
    time.sleep(0.5)
    with addblock:
        count+=1

addblock = threading.Lock()
threads = []
for i in range(1000):
    thread = threading.Thread(target=adder, args=(addblock,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(count)
