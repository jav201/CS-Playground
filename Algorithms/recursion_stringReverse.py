
string = 'abcde'

def reverse(string):

    if len(string) == 1:
        return string[0]
    # Understand the subproblem. if we can address the first reversal, then think
    # as somebody else has already thought of the solution, so the function can handle 
    # the rest of the problem... then identify and write the base case.    
    return reverse(string[1::]) + string[0]

print(reverse(string))