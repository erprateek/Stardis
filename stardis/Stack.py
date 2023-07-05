from stardis import Stack

"""
Stack Module

This module implements a stack data structure using the Stack class.
A stack follows the Last-In-First-Out (LIFO) principle, where the last item pushed is the first to be popped.

Classes:
- Stack: Represents a stack data structure.

"""

class Stack:
    """
    Stack Class

    A class representing a stack data structure.

    Methods:
    - push(elem): Pushes an element onto the top of the stack.
    - pop(): Removes and returns the top element from the stack.
    - isEmpty(): Checks if the stack is empty.
    - isInStack(item): Checks if an item is present in the stack.
    - reverse(): Returns a new stack with the elements in reverse order.

    """

    class Node:
        """
        Node Class

        A class representing a node in the stack.

        Attributes:
        - item: The value of the node.
        - next: The reference to the next node.

        """

        def __init__(self, object, Next):
            """
            Node initialization.

            Args:
            - object: The value to be stored in the node.
            - Next: The reference to the next node.

            """
            self.item = object
            self.next = Next

    def __init__(self):
        """
        Stack initialization.

        Initializes an empty stack.

        """
        self.top = None
        self.bottom = None
        self.size = 0

    def push(self, elem):
        """
        Push an element onto the stack.

        Args:
        - elem: The element to be pushed onto the stack.

        """
        newNode = self.Node(elem, None)
        if self.top is None and self.bottom is None and self.size == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.size += 1

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
        The top element from the stack.

        """
        curNode = self.top
        self.top = self.top.next
        self.size -= 1
        return curNode.item

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
        True if the stack is empty, False otherwise.

        """
        return self.size == 0

    def isInStack(self, item):
        """
        Check if an item is present in the stack.

        Args:
        - item: The item to be searched in the stack.

        Returns:
        True if the item is present in the stack, False otherwise.

        """
        if self.isEmpty():
            return False
        curNode = self.top
        while curNode is not None and curNode.next is not None:
            if curNode.item == item:
                return True
            else:
                curNode = curNode.next

    def reverse(self):
        """
        Reverse the stack.

        Returns:
        A new stack with the elements in reverse order.

        """
        import copy
        if self.isEmpty() or self.size == 1:
            return copy.copy(self)
        copyStack = copy.copy(self)
        newStack = Stack()
        while not copyStack.isEmpty():
            newStack.push(copyStack.pop())
        return newStack

