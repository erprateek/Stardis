from stardis import BinaryTree

class BinaryTree:
    class Node:
        def __init__(self,value):
            self.value = value
            self.left = None
            self.right = None
            self.level = None
            
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, item):
        if self.value == item:
            return #we do nothing because the item is already here
        else:
            if item < self.value:
                if self.left != None:
                    self.left.insert(item)
                else:
                    self.left = self.Node(item)
            else:
                if self.right != None:
                    self.right.insert(item)
                else:
                    self.right = self.Node(item)
                    
    def highest(self):
        """Returns the highest value in the tree"""
        if self.right != None:
            return self.right.highest()
        else:
            return self.value
    
    def lowest(self):
        """Returns the smallest value in the tree"""
        if self.left != None:
            return self.left.lowest()
        else:
            return self.value
    
    def delete(self, value):
        #### If the current node has the value
        if value == self.value:
            if self.left != None:
                #### Set the value to the highest value in the left subtree
                #### Delete that value
                self.value = self.left.highest()
                self.left.delete(self.value)
            elif self.right != None:
                self.value = self.right.lowest()
                self.right.delete(self.value)
            else:
                return None
        else:
            """Find which subtree has the value"""
            if value < self.value and self.left != None:
                self.left = self.left.delete(value)
            if value > self.value and self.right != None:
                self.right = self.right.delete(value)
            return self
