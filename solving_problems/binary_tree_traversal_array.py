"""
Print array representation of a binary tree
Input : below tree
            1
          /   \
         2      3
        / \    / \
       4   5  6   7
                /   \
               8     9

            or 

            A
          /   \
         B      C
        / \    / \
       D   E  F   G

Output for levelorder traversal:
[1,2,3,4,5,6,7,None,None,None,None,None,None,8,9]
or 
[A,B,C,D,E,F,G]
"""

from collections import deque

# utility function for node creation


class NewNode():
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


# Driver Code
if __name__ == '__main__':
    root = NewNode(1)
    root.left = NewNode(2)
    root.right = NewNode(3)
    root.left.left = NewNode(4)
    root.left.right = NewNode(5)
    root.right.left = NewNode(6)
    root.right.right = NewNode(7)
    root.right.right.left = NewNode(8)
    root.right.right.right = NewNode(9)

# auxilliary data structure (queue) for traversing the binary tree and
# printing array representation


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            # None data value is a way of saving a given tree structure
            # and indicate there is no children for this node (therefore it is a leaf)
            if self.items[-1] == None:
                return self.items[-1]
            else:
                return self.items[-1].data

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class PrintTree(object):
    def __init__(self, root):
        self.levels = getHeight(root)

    def representation(self, traversal_type, array, levels=None):
        if traversal_type == "preorder":
            return self.preorder_print(root, array, levels)
        elif traversal_type == "inorder":
            return self.inorder_print(root, array, levels)
        elif traversal_type == "postorder":
            return self.postorder_print(root, array, levels)
        elif traversal_type == "levelorder":
            return self.levelorder_print(root, array)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, array, levels):
        """Root->Left->Right
        In this traversal method, the root node is visited first, 
        then the left subtree and finally the right subtree."""
        if start:
            array.append(start.data)
            self.preorder_print(start.left, array, levels - 1)
            self.preorder_print(start.right, array, levels - 1)
        elif levels > 0:
            array.append(None)
        return array

    def inorder_print(self, start, array, levels):
        """Left->Root->Right
        the left subtree is visited first, then the root and later
        the right sub-tree. Every node may represent a subtree itself.
        The output will produce sorted key values in an ascending order."""

        if start:
            self.inorder_print(start.left, array, levels - 1)
            array.append(start.data)
            self.inorder_print(start.right, array, levels - 1)
        elif levels > 0:
            array.append(None)
        return array

    def postorder_print(self, start, array, levels):
        """Left->Right->Root
        The root node is visited last. 
        First we traverse the left subtree, then 
        the right subtree and finally the root node."""
        if start:
            self.postorder_print(start.left, array, levels - 1)
            self.postorder_print(start.right, array, levels - 1)
            array.append(start.data)
        elif levels > 0:
            array.append(None)
        return array

    def levelorder_print(self, start, array):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        while len(queue) > 0:
            array.append(queue.peek())
            node = queue.dequeue()
            isNode = isinstance(node, NewNode)
            if isNode:
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
                if node.left == None:
                    queue.enqueue(None)
                if node.right == None:
                    queue.enqueue(None)
        return array


def getHeight(node):
    return 0 if not node else max(getHeight(node.left), getHeight(node.right)) + 1


printedTree = PrintTree(root)
levels = printedTree.levels

"""
Input : below tree
            1
          /   \
         2      3
        / \    / \
       4   5  6   7
                /   \
               8     9

            or 

            A
          /   \
         B      C
        / \    / \
       D   E  F   G

"""
print(f'levelorder traversal: {printedTree.representation("levelorder", [])}')
#[1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, None, None, None, None]
# or A → B → C → D → E → F → G
print(
    f'preorder traversal: {printedTree.representation("preorder", [], levels)}')
# Root->Left->Right: [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, 8, 9]
# or A → B → D → E → C → F → G
print(
    f'inorder traversal: {printedTree.representation("inorder", [], levels)}')
# Left->Root->Right: [None, 4, None, 2, None, 5, None, 1, None, 6, None, 3, 8, 7, 9]
# or D → B → E → A → F → C → G
print(
    f'postorder traversal: {printedTree.representation("postorder", [], levels)}')
# Left->Right->Root: [None, 4, None, 2, None, 5, None, None, 6, None, 3, 8, 7, 9, 1]
# or D → E → B → F → G → C → A
