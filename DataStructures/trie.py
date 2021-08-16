
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for char in word:
            #Advance one level deeper in the trie when the char exists
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                # Char does not exist, create the node
                newNode = TrieNode()
                currentNode.children[char] = newNode
                # Go to the new node
                currentNode = currentNode.children[char]
        # Add finish char and None as next node
        currentNode.children['*'] = None

    def search(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
        return currentNode

    def collectAllWords(self, node=None, word='', words=[]):
        # Begin at root or specified node
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            if key == '*':
                words.append(word)
            else:
                self.collectAllWords(childNode, word+key, words)
        return words

    def autocomplete(self, word):
        currentNode = self.search(word)
        if not currentNode:
            return None
        # we have to pass an empy list, otherwise previous searchs within a
        # looped program get appended
        return [word+x for x in self.collectAllWords(currentNode, words=[])]

myTrie = Trie()

# Read file and insert words in the trie
with open('DataStructures/words.txt','r') as fh:
    line = fh.readline()
    while line:
        myTrie.insert(line.strip('\n'))
        line = fh.readline()

print('Type words prefix to search...\nTo exit type "ex_"\n', end='')
while True:
    print('')
    wordIn = input()
    if wordIn == 'ex_':
        print('Terminating program...')
        exit()
    else:
        print(myTrie.autocomplete(wordIn))