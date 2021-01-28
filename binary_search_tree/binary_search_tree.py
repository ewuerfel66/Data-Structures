import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Insertion requires a tree to already exist
        # if value less than self.value go left, new tree/node if empty,
        # otherwise keep going
        if value < self.value:
            # Create a new tree if necessary
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        # If greater than or equal go to right
        # make new tree/node if empty otherwise
        # keep going (recursion)
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        if self.right is None:
            return self.value

        elif self.right:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        # Check the left side
        if self.left:
            self.left.for_each(cb)

        # Check the right side
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.value:
            # Check left side
            if node.left:
                node.in_order_print(node.left)

            print(node.value)

            # Check the right side
            if node.right:
                node.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Create Queue
        queue = Queue()

        # Add root
        queue.enqueue(node)

        while queue.size > 0:
            new_node = queue.dequeue()
            print(new_node.value)

            if new_node.left:
                queue.enqueue(new_node.left)
            
            if new_node.right:
                queue.enqueue(new_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Create stack
        stack = Stack()

        # Add root
        stack.push(node)

        while stack.size > 0:
            new_node = stack.pop()
            print(new_node.value)

            if new_node.left:
                stack.push(new_node.left)

            if new_node.right:
                stack.push(new_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
