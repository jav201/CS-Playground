# Create a linked List
from ast import NodeTransformer
from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    
class LinkedList:
    
    def __init__(self, node=None):
        self.firstNode = node
    
    def read(self, index):
        currentNode = self.firstNode
        currentIndex = 0
        while currentIndex < index:
            currentNode = self.nextNode
            currentIndex += 1
            if currentNode is None:
                return None
        return currentNode

    def insertAtIndex(self, index, data):
        currentNode = self.firstNode
        currentIndex = 0
        # Insert at first position
        if index == 0:
            newNode = Node(data)
            newNode.nextNode = self.firstNode
            self.firstNode = newNode
        while currentIndex < index-1:
            if currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
                currentIndex += 1
            else:
                print('Invalid Index')
                return
        newNode = Node(data)
        newNode.nextNode = currentNode.nextNode
        currentNode.nextNode = newNode
        
    def deleteAtIndex(self, index):
        currentNode = self.firstNode
        currentIndex = 0
        # Delete Base Node
        if index == 0 and currentNode.nextNode is not None:
            self.firstNode = self.firstNode.nextNode
            return
        while currentIndex < index-1:
            if currentNode is not None:
                currentNode = currentNode.nextNode
                currentIndex += 1
            else:
                print('Invalid Index')
                return
        nodeToDelete = currentNode.nextNode
        currentNode.nextNode = nodeToDelete.nextNode
        del nodeToDelete
        return
    
    def insertAtEnd(self, data):
        currentNode = self.firstNode
        while currentNode.nextNode:
            currentNode = currentNode.nextNode
        newNode = Node(data)
        currentNode.nextNode = newNode

    def printData(self):
        currentNode = self.firstNode
        while currentNode.nextNode:
            print(currentNode.data, end=' ')
            currentNode = currentNode.nextNode
        print(currentNode.data)

# Excercise to delete duplicates on a linked list 
# Create linked list 
baseNode = Node('a')
ll = LinkedList(baseNode)
ll.insertAtEnd('f')
ll.insertAtEnd('d')
ll.insertAtEnd('e')
ll.insertAtEnd('c')
ll.insertAtEnd('b')
ll.insertAtEnd('b')
ll.insertAtEnd('c')
ll.insertAtEnd('b')
ll.insertAtEnd('g')
ll.printData()


# Delete duplicates
dictBuffer = {}
currentNode = ll.firstNode
currentData = currentNode.data
dictBuffer[currentData] = 1
while currentNode.nextNode is not None:
    nextData = currentNode.nextNode.data
    if dictBuffer.get(nextData) is not None:
        dictBuffer[nextData] += 1
        nodeToDelete = currentNode.nextNode
        currentNode.nextNode = nodeToDelete.nextNode
        del nodeToDelete
    else:
        dictBuffer[nextData] = 1
        currentNode = currentNode.nextNode

ll.printData()

# Return the kth to last element
# TODO