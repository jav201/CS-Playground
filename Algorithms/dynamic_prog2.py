# Longest common subsequence
# word1 = 'fosh'
# word2 = 'fort'

word1 = 'comadre'
word2 = 'comadreja'
# word2 = 'jerecuaro'

word_matrix = [ [ 0 for x in range(len(word2)) ] for _ in range(len(word1)) ]

for i in range(len(word1)):
    for j in range(len(word2)):
        # Check if the letter matches
        if word1[i] == word2[j]:
            word_matrix[i][j] = 1 + word_matrix[i-1][j-1]
        else:
            word_matrix[i][j] = max(word_matrix[i-1][j], word_matrix[i][j-1])

# Some fancy printing            
print('  ',end='')
for i in word2: print(' '+i+' ', end='')
print('')
for i,l in zip(word_matrix, list(word1)): print(l,i)
print('\n'+'Max value or highest similar coefficient:')
print(max([max(x) for x in word_matrix]))
