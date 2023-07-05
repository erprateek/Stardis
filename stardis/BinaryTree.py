from stardis import BinaryTree

"""
BinaryTree Module

This module implements a binary tree data structure using the BinaryTree class.
A binary tree is a hierarchical structure where each node has at most two children, referred to as the left child and the right child.

Classes:
- BinaryTree: Represents a binary tree data structure.

"""

class BinaryTree:
    """
    BinaryTree Class

    A class representing a binary tree data structure.

    Methods:
    - insert(item): Inserts an item into the binary tree.
    - highest(): Returns the highest value in the binary tree.
    - lowest(): Returns the smallest value in the binary tree.
    - delete(value): Deletes a value from the binary tree.

    """

    class Node:
        """
        Node Class

        A class representing a node in the binary tree.

        Attributes:
        - value: The value of the node.
        - left: The reference to the left child node.
        - right: The reference to the right child node.
        - level: The level of the node in the binary tree.

        """

        def __init__(self, value):
            """
            Node initialization.

            Args:
            - value: The value to be stored in the node.

            """
            self.value = value
            self.left = None
            self.right = None
            self.level = None

    def __init__(self):
        """
        BinaryTree initialization.

        Initializes an empty binary tree.

        """
        self.root = None
        self.size = 0

    def insert(self, item):
        """
        Insert an item into the binary tree.

        Args:
        - item: The item to be inserted.

        """
        if self.root is None:
            self.root = self.Node(item)
        else:
            self._insert_recursive(item, self.root)

    def _insert_recursive(self, item, current_node):
        """
        Recursively insert an item into the binary tree.

        Args:
        - item: The item to be inserted.
        - current_node: The current node being considered during the insertion.

        """
        if item < current_node.value:
            if current_node.left is not None:
                self._insert_recursive(item, current_node.left)
            else:
                current_node.left = self.Node(item)
        else:
            if current_node.right is not None:
                self._insert_recursive(item, current_node.right)
            else:
                current_node.right = self.Node(item)

    def highest(self):
        """
        Return the highest value in the binary tree.

        Returns:
        The highest value in the binary tree.

        """
        if self.root is not None:
            return self._highest_recursive(self.root)
        else:
            return None

    def _highest_recursive(self, current_node):
        """
        Recursively find the highest value in the binary tree.

        Args:
        - current_node: The current node being considered during the traversal.

        Returns:
        The highest value in the binary tree.

        """
        if current_node.right is not None:
            return self._highest_recursive(current_node.right)
        else:
            return current_node.value

    def lowest(self):
        """
        Return the smallest value in the binary tree.

        Returns:
        The smallest value in the binary tree.

        """
        if self.root is not None:
            return self._lowest_recursive(self.root)
        else:
            return None

    def _lowest_recursive(self, current_node):
        """
        Recursively find the smallest value in the binary tree.

        Args:
        - current_node: The current node being considered during the traversal.

        Returns:
        The smallest value in the binary tree.

        """
        if current_node.left is not None:
            return self._lowest_recursive(current_node.left)
        else:
            return current_node.value

    def delete(self, value):
        """
        Delete a value from the binary tree.

        Args:
        - value: The value to be deleted.

        Returns:
        The root node of the modified binary tree.

        """
        if self.root is not None:
            self.root = self._delete_recursive(value, self.root)

    def _delete_recursive(self, value, current_node):
        """
        Recursively delete a value from the binary tree.

        Args:
        - value: The value to be deleted.
        - current_node: The current node being considered during the deletion.

        Returns:
        The node resulting from the deletion.

        """
        if value == current_node.value:
            if current_node.left is not None:
                current_node.value = self._highest_recursive(current_node.left)
                current_node.left = self._delete_recursive(current_node.value, current_node.left)
            elif current_node.right is not None:
                current_node.value = self._lowest_recursive(current_node.right)
                current_node.right = self._delete_recursive(current_node.value, current_node.right)
            else:
                return None
        else:
            if value < current_node.value and current_node.left is not None:
                current_node.left = self._delete_recursive(value, current_node.left)
            if value > current_node.value and current_node.right is not None:
                current_node.right = self._delete_recursive(value, current_node.right)
            return current_node

