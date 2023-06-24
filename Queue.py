class Queue:
    class Node:
        def __init__(self,object,Next):
            self.item = object
            self.next = Next
    
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
        
    def enqueue(self,elem):
        newNode = self.Node(elem,None)
        if (self.front is None) and (self.back is None) and (self.size == 0):
            self.front = newNode
            self.back = newNode
        else:
            self.back.next = newNode
        self.size = self.size+1
    
    def dequeue(self):
        self.front = self.front.next
        self.size = self.size-1
    
    def isEmpty(self):
        return (self.size == 0)
    
    def isInQueue(self,item):
        if(self.isEmpty()):
            return False
        curNode = self.front
        while(curNode is not None and curNode.next is not None):
            if(curNode.item == item):
                return True
            else:
                curNode = curNode.next