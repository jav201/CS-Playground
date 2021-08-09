class Node:
    def __init__(self, dataValue = None):
        self.dataValue = dataValue
        self.nextValue = None

class LinkedList:
    def __init__(self):
        self.headValue = None
    
    def __repr__(self):
        listOut = []
        value = self.headValue
        while value != None:
            listOut.append(value.dataValue)
            value = value.nextValue
        return str(listOut)
    
    def begginingInsert(self, newData):
        newNode = Node(newData)
        newNode.nextValue = self.headValue
        self.headValue = newNode

    def endInsert(self, newData):
        newNode = Node(newData)
        if self.headValue == None:
            self.headValue = newNode
            return
        nodeIter = self.headValue
        while nodeIter.nextValue:
            nodeIter = nodeIter.nextValue
        nodeIter.nextValue = newNode
        


llist = LinkedList()
llist.headValue = Node('Monday')
n2 = Node('Tuesday')
n3 = Node('Wednesday')

llist.headValue.nextValue = n2
n2.nextValue = n3
llist.begginingInsert('Sunday')
llist.endInsert('Thursday')
print(llist)