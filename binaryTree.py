
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right    

    def insert(self, value):
        if self.value == value:
            print('Dupliccated value {0} ignored'.format(value))
        elif self.value:
            if value < self.value:
                if self.leftChild is None:
                    self.leftChild = TreeNode(value)
                else:
                    self.leftChild.insert(value)
            elif value > self.value:
                if self.rightChild is None:
                    self.rightChild = TreeNode(value)
                else:
                    self.rightChild.insert(value)
        else:
            self.value = TreeNode(value)

    def search(self, value):
        if self.value == None or self.value == value:
            return self
        elif self.value > value and self.leftChild is not None:
            return self.leftChild.search(value)
        elif self.value < value and self.leftChild is not None:
            return self.rightChild.search(value)

    def printTree(self):
        if self.leftChild:
            self.leftChild.printTree()
        print(self.value)
        if self.rightChild:
            self.rightChild.printTree()

    # TODO implement delete 


# node1 = TreeNode(25)
# node2 = TreeNode(75)
# root = TreeNode(50, node1, node2)


# listIn = [25, 75, 10, 33, 56, 89, 4, 11, 30, 40, 52, 61, 82, 95]
# root = TreeNode(50, TreeNode(25), TreeNode(75))
# for _ in listIn:
#     root.insert(_,)

# root.printTree()
# print(root.search(4) is None)
# print(root.search(4))

root = TreeNode(50)
root.insert(25)
root.insert(75)
root.insert(10)
root.insert(33)
root.insert(56)
root.printTree()

print(root.search(4))


