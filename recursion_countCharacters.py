
def countCharacters(string, char):
    # Base case
    if len(string) == 1:
        if string[0] == char:
            return 1
        return 0
    elif string[0] == char:
        return 1 + countCharacters(string[1::], char)
    return countCharacters(string[1::], char)

print(countCharacters('axbxcxd','x'))