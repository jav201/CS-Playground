# Longest common substring
word1 = 'caracuaro'
word2 = 'paztcuaro'
word2 = 'jerecuaro'

word_matrix = [ [ 0 for x in range(len(word2)) ] for _ in range(len(word1)) ]

for i in range(len(word1)):
    for j in range(len(word2)):
        # Check if the letter matches
        if word1[i] == word2[j]:
            word_matrix[i][j] = 1 + word_matrix[i-1][j-1]
        else:
            word_matrix[i][j] = 0
print(word_matrix)
print(max([max(x) for x in word_matrix]))
