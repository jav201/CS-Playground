class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self, node=None):
        self.firstNode = node

    def read(self, index) -> Node:
        """Returns the node at index; else, None"""
        currentNode = self.firstNode
        currentIndex = 0
        while currentIndex < index:
            currentNode = currentNode.nextNode
            currentIndex += 1
            if currentNode is None:
                return None
        return currentNode
    
    def insertAtIndex(self, index, data):
        currentNode = self.firstNode
        currentIndex = 0
        # Insert at root
        if index == 0:
            newNode = Node(data)
            newNode.nextNode = self.root
            self.root = newNode
        # Insert at a different index| index -1 because
        # we need to place the new node using nextNode
        while currentIndex < (index - 1):
            if currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
                index += 1
            else:
                print('Invalid Index')
                return
        newNode = Node(data)
        newNode.nextNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def deleteAtIndex(self, index):
        currentNode = self.firstNode
        if index == 0 and currentNode.nextNode is not None:
            self.firstNode = self.firstNode.nextNode
        currentIndex = 0
        while currentIndex < (index - 1):
            if currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
                currentIndex += 1
            else:
                print('Invalid index')
                return
        nodeToDelete = currentNode.nextNode
        currentNode.nextNode = nodeToDelete.nextNode
        del nodeToDelete

    def insertAtEnd(self, data):
        currentNode = self.firstNode
        while currentNode.nextNode:
            currentNode = currentNode.nextNode
        newNode = Node(data)
        currentNode.nextNode = newNode

    def printData(self):
        currentNode = self.firstNode
        while currentNode.nextNode:
            print(currentNode.data)
            currentNode = currentNode.nextNode
        print(currentNode.data)


newNode = Node('prro')
newLL = LinkedList(newNode)
newLL.insertAtIndex(1,'otroPrro')
newLL.printData()
newLL.deleteAtIndex(3)
newLL.printData()
newLL.insertAtEnd('a')
newLL.insertAtEnd('b')
newLL.insertAtEnd('c')
newLL.printData()
newLL.deleteAtIndex(2)
newLL.printData()