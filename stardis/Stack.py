from stardis import Stack

class Stack:
    class Node:
        def __init__(self,object,Next):
            self.item = object
            self.next = Next
    
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0
        
    def push(self,elem):
        newNode = self.Node(elem,None)
        if (self.top is None) and (self.bottom is None) and (self.size == 0):
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.size = self.size+1
    
    def pop(self):
        curNode = self.top
        self.top = self.top.next
        self.size = self.size-1
        return curNode.item
    
    def isEmpty(self):
        return (self.size == 0)
    
    def isInStack(self,item):
        if(self.isEmpty()):
            return False
        curNode = self.top
        while(curNode is not None and curNode.next is not None):
            if(curNode.item == item):
                return True
            else:
                curNode = curNode.next
    
    def reverse(self):
        import copy
        if(self.isEmpty() or self.size == 1):
            return copy.copy(self)
        copyStack = copy.copy(self)
        newStack = Stack()
        while copyStack.isEmpty() == False:
            newStack.push(copyStack.pop())
        return newStack
