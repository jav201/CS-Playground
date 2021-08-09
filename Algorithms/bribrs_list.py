list_in = [2, 1, 5, 3, 4]
def findout(list_in):
    n = len(list_in)
    for i in range(0,n-1):
        count = 0
        for j in range(0,n-i-1):
            if list_in[j] > list_in[j+1]:
                # swap
                list_in[j], list_in[j+1] = list_in[j+1], list_in[j]
                count += 1
        print(i, count)
findout(list_in)  