import pytest
from stardis import Stack, Queue, BinaryTree

# Test cases for Stack class
def test_stack_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size == 3

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.size == 2

def test_stack_is_empty():
    stack = Stack()
    assert stack.isEmpty() == True
    stack.push(1)
    assert stack.isEmpty() == False

def test_stack_is_in_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.isInStack(2) == True
    assert stack.isInStack(4) == False

def test_stack_reverse():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    reversed_stack = stack.reverse()
    assert reversed_stack.pop() == 1
    assert reversed_stack.pop() == 2
    assert reversed_stack.pop() == 3

# Test cases for Queue class
def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size == 3

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    assert queue.size == 2

def test_queue_is_empty():
    queue = Queue()
    assert queue.isEmpty() == True
    queue.enqueue(1)
    assert queue.isEmpty() == False

def test_queue_is_in_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.isInQueue(2) == True
    assert queue.isInQueue(4) == False

# Test cases for BinaryTree class
def test_binary_tree_insert():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    assert binary_tree.root.value == 5
    assert binary_tree.root.left.value == 3
    assert binary_tree.root.right.value == 7

def test_binary_tree_highest():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    assert binary_tree.highest() == 7

def test_binary_tree_lowest():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    assert binary_tree.lowest() == 3

def test_binary_tree_delete():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.delete(5)
    assert binary_tree.root.value == 7
    assert binary_tree.root.left.value == 3
    assert binary_tree.root.right is None

