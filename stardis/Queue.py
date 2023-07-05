from stardis import Queue

"""
Queue Module

This module implements a queue data structure using the Queue class.
A queue follows the First-In-First-Out (FIFO) principle, where the first item enqueued is the first to be dequeued.

Classes:
- Queue: Represents a queue data structure.

"""

class Queue:
    """
    Queue Class

    A class representing a queue data structure.

    Methods:
    - enqueue(elem): Enqueues an element at the back of the queue.
    - dequeue(): Dequeues the element at the front of the queue.
    - isEmpty(): Checks if the queue is empty.
    - isInQueue(item): Checks if an item is present in the queue.

    """

    class Node:
        """
        Node Class

        A class representing a node in the queue.

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
        Queue initialization.

        Initializes an empty queue.

        """
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, elem):
        """
        Enqueue an element at the back of the queue.

        Args:
        - elem: The element to be enqueued.

        """
        newNode = self.Node(elem, None)
        if self.front is None and self.back is None and self.size == 0:
            self.front = newNode
            self.back = newNode
        else:
            self.back.next = newNode
        self.size += 1

    def dequeue(self):
        """
        Dequeue the element at the front of the queue.

        """
        self.front = self.front.next
        self.size -= 1

    def isEmpty(self):
        """
        Check if the queue is empty.

        Returns:
        True if the queue is empty, False otherwise.

        """
        return self.size == 0

    def isInQueue(self, item):
        """
        Check if an item is present in the queue.

        Args:
        - item: The item to be searched in the queue.

        Returns:
        True if the item is present in the queue, False otherwise.

        """
        if self.isEmpty():
            return False
        curNode = self.front
        while curNode is not None and curNode.next is not None:
            if curNode.item == item:
                return True
            else:
                curNode = curNode.next

