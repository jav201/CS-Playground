# Interesting fact: The binary tree can't have a class for the tree
# the insert function needs to be out of the structure
# otherwise, the function can't go deeper within the branches. 
# The use of None makes this difficult... there are ways to go around this...
# maybe using a special character but such solution is not the simplest...
# might be worth to explore that later...
class treeNode:
    def __init__(self,value=None,left = None,right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def insert(value, node) -> None:
    currentNode = node
    # If less than value, go left
    if value < currentNode.value:
        if currentNode.left is None:
            currentNode.left = treeNode(value)
        else:
            insert(value, currentNode.left)
    # If greather than value, go right
    elif value > currentNode.value:
        if currentNode.right is None:
            currentNode.right = treeNode(value)
        else:
            insert(value, currentNode.right)

def isIn(value, node):
    if node is None:
        return False
    elif value == node.value:
        return True
    elif value < node.value:
        return isIn(value, node.left)
    else: # value > node.value
        return isIn(value, node.right)

def search(value, node):
    if node is None or value == node.value:
        return node
    elif value < node.value:
        return search(value, node.left)
    else: # value > node.value
        return search(value, node.right)

def treePrint(value=None, node=None):
    if node.left is not None:
        treePrint(node.value, node.left)
    print(node.value)
    if node.right is not None:
        treePrint(node.value, node.right)
    
def lift(node, nodeToDelete):
    if node.left:
        node.left = lift(node.left, nodeToDelete)
        return node
    else:
        nodeToDelete.value = node.value
        return node.right

def delete(valueToDelete, node):
    # Base case, node does not exists
    if node is None:
        return None
    # If value is less than node value, go left
    elif valueToDelete < node.value:
        node.left = delete(valueToDelete, node.left)
        return node
    # If value is greather than node value, go right
    elif valueToDelete > node.value:
        node.right = delete(valueToDelete, node.right)
        return node
    # Found the node to delte, check for children
    elif valueToDelete == node.value:
        # If there are no left child, and there is a right child
        # The right child will become the left child of the former 
        # parent of the deleted child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            node.right = lift(node.right, node)
            return node
    

myTree = treeNode(50)
insert(25, myTree)
insert(75, myTree)
insert(10, myTree)
insert(33, myTree)
insert(56, myTree)
insert(89, myTree)
insert(4,  myTree)
insert(11, myTree)
insert(30, myTree)
insert(40, myTree)
insert(52, myTree)
insert(61, myTree)
insert(82, myTree)
insert(95, myTree)
print(isIn(10, myTree))
print(search(25,myTree))
print(search(30,myTree))
treePrint(node=myTree)
delete(75,myTree)
print()
treePrint(node=myTree)
