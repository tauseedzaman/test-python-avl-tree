def getStudentNumber():
    # This method must return your name EXACTLY as D2L presents it.
    # If this does not work, you will fail this lab.
    return "123456789"


class MyBST:
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

    def updateHeight(self):
        # Update the height of this node
        self.height = max(
            -1 if self.left is None else self.left.updateHeight(),
            -1 if self.right is None else self.right.updateHeight()
        ) + 1
        return self.height

    def __contains__(self, data):
        # Returns true if data is in this node or a node descending from it
        # This overloaded method allows you to use the python operator 'in'
        if self.data == data:
            return True
        # Key is greater than root's key
        if self.right is not None and self.data < data:
            return self.right.__contains__(data)
        elif self.data < data:
            return False

        # Key is smaller than root's key
        if self.left is not None and self.data > data:
            return self.left.__contains__(data)
        elif self.data > data:
            return False

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

    def findSmallest(self):
        if self.left is None:
            return self.data
        else:
            return self.left.findSmallest()
        # Return the value of the smallest node

    def findLargest(self):
        if self.right is None:
            return self.data
        else:
            return self.right.findLargest()
        # Return the value of the largest node

    def remove(self, data):
        # Find the data in the input parameter and remove it
        # Ensures that the tree remains a valid Binary Search Tree
        # Return this node after data has been deleted
        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if data < self.data:
            if self.left is None:
                return None
            self.left = self.left.remove(data)

        # If the key to be deleted
        # is greater than the root's key
        # then it lies in right subtree
        elif data > self.data:
            if self.right is None:
                return None
            self.right = self.right.remove(data)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:
            if self.left is None and self.right is None:
                # The node has no children -- it is a leaf node. Just delete.
                return None

                # If the node has only one children, simply return that child.
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            if not self.promote_right:
                parent, node = self, self.left
                while node.right is not None:
                    parent, node = node, node.right
                if parent.left is node:
                    # This check is necessary, because if the left subtree has only
                    # node, `node` would be `self.left`.
                    parent.left = None
                else:
                    parent.right = None
            else:
                parent, node = self, self.right
                while node.left is not None:
                    parent, node = node, node.left
                if parent.right is node:
                    # This check is necessary, because if the left subtree has only
                    # node, `node` would be `self.left`.
                    parent.right = None
                else:
                    parent.left = None
            # Now, `node` is the rightmost node in the left subtree, and
            # `parent` its parent node. Instead of replacing `self`, we change
            # its attributes to match the value of `node`.

            self.data = node.data

        return self


# Bonus functions to help you debug
def printTree_(tree, prefix):
    if tree.getLeft() is not None:
        printTree_(tree.getLeft(), prefix + "+ ")
    print(f"{prefix}{tree.data}")
    if tree.getRight() is not None:
        printTree_(tree.getRight(), prefix + "- ")


def printTree(tree):
    printTree_(tree, "")


if __name__ == "__main__":
    # Implement your testing logic here.
    # This code will not execute if this file is loaded as a library.
    pass
