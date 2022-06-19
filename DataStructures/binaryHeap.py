class Heap:
    def __init__(self):
        self.data = []

    def rootNode(self):
        return self.data[0]

    def lastNode(self):
        return self.data[-1]

    def insert(self, value):
        self.data.append(value)
        newNodeIndex = len(self.data) - 1
        while newNodeIndex > 0 and self.data[newNodeIndex] > self.data[self.parentIndex(newNodeIndex)]:
            # Swap the nodes
            self.data[self.parentIndex(newNodeIndex)], self.data[newNodeIndex] = \
                self.data[newNodeIndex], self.data[self.parentIndex(newNodeIndex)]
            newNodeIndex = self.parentIndex(newNodeIndex)

    def hasGreaterChild(self, index):
        pass

    def getLarferChildIndex(self, index):
        pass

    def delete(self):
        # Delete the top priority
        self.data.pop(0)
        trickleNodeIndex = 0
        while self.hasGreaterChild(trickleNodeIndex):
            largerChildIndex = self.getLargerChildIndex(trickleNodeIndex)
            # Swap nodes
            self.data[trickleNodeIndex], self.data[largerChildIndex] = \
                self.data[largerChildIndex], self.data[trickleNodeIndex]
            trickleNodeIndex = largerChildIndex

    @staticmethod
    def leftChildIndex(parentIndex):
        return (parentIndex * 2) + 1

    @staticmethod
    def rightChildIndex(parentIndex):
        return (parentIndex * 2) + 1

    @staticmethod 
    def parentIndex(childIndex):
        return int(childIndex / 2)
    
    