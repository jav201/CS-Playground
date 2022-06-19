The redirect file uses the teststreams to catch the data from data streams. In this way python can fetch the data flows:
Data Flow:

>>> from redirect import redirect
>>> from teststreams import interact
>>> (result, output) = redirect(interact, (), {}, '4\n5\n6\n')
>>> print(result)
None
>>> output
'Hello stream world!\nEnter a number>4 squared is 16\nEnter a number>5 squared is 25\nEnter a number>6 squared is 36\nEnter a number>Bye!\n'
>>> for line in output.splitlines(): print(line)
... 
Hello stream world!
Enter a number>4 squared is 16
Enter a number>5 squared is 25
Enter a number>6 squared is 36
Enter a number>Bye!