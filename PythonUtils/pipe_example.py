# # Pipes
# import os

# # spawn the ID from this rogram process with os.getpdi
# print("PID parent {}".format(os.getpid()))
# # pid is the copy of this program process
# pid = os.fork()
# print("PID child {}".format(pid))

# import os

# pid = os.fork()

# if pid > 0:
#     print("This is written by the parent process {}".format(os.getpid()))
# else:
#     print("This is written by the child process {}".format(os.getpid()))

import os

NUM_PROC  = 5
children = []

for process in range(NUM_PROC):
    pid = os.fork()
    if pid > 0: 
        print("This is the parent process {}".format(os.getpid()))
        children.append(pid)
    else: 
        print("This is the child process {}".format(os.getpid()))
        os._exit(0)

# This line permits the parent process to wait until all children are closed
for proc in children: os.waitpid(proc, 0)
print("Parent process is closing")