def getStudentNumber():
    return "Example Solution"


class MyBST():
    def __init__(self, data, promote_right=True):
        # Initialize this node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

        # Set promote_right to TRUE if you are implementing
        # the promotion of the smallest node on left subtree,
        # Otherwise, set it to FALSE
        self.promote_right = promote_right

    def getLeft(self):
        # Return the left child of this node, or None
        return self.left

    def getRight(self):
        # Return the right child of this node, or None
        return self.right

    def getData(self):
        # Return the data contained in this node
        return self.data

    def getHeight(self):
        # Return the height of this node
        return self.height
    
    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = MyBST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = MyBST(data)
        self.updateHeight()
        return self

    # COPY THIS FROM LAB 3
    # OR IMPLEMENT IT HERE IF YOU DID NOT DO LAB 3

    def updateHeight(self):
        # Update the height of this node
        pass

    def __contains__(self, data):
        # Returns true if data is in this node or a node descending from it
        pass

    def findSmallest(self):
        # Find the smallest node descending from this node
        pass
    
    def findLargest(self):
        # Find the largest node descending from this node
        pass
    
    # END COPY



class MyAVL(MyBST):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)
        self.bf = 0

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid AVL tree
        # Return the node in this node's position after data has been inserted
        if data < self.data:
            if self.left:
                self.left = self.left.insert(data)
            else:
                self.left = MyAVL(data)
        else:
            if self.right:
                self.right = self.right.insert(data)
            else:
                self.right = MyAVL(data)
        self.updateHeight()
        self.bf = self.getBalanceFactor()
        new = self.reBalance()
        return new

    def leftRotate(self):
        # Perform a left rotation on this node and return the new node in its spot
        pass

    def rightRotate(self):
        # Perform a right rotation on this node and return the new node in its spot
        pass
    
    def remove(self, data):
        # Remove data from the tree descending from this node and return the new node in its spot
        pass

    def reBalance(self):
        # Apply any rotations needed from this node and return the node in its spot
        pass

    def getBalanceFactor(self):
        # Return the balance factor of this node
        pass



def printTree_(tree, prefix):
    if tree.getLeft() is not None:
        printTree_(tree.getLeft(),prefix+"+ ")
    print(f"{prefix}{tree.data}")
    if tree.getRight() is not None:
        printTree_(tree.getRight(),prefix+"- ")

def printTree(tree):
    printTree_(tree,"")

    
# Put any testing code here
# Submit this code with no print statements above this line
if __name__=="__main__":
    pass
