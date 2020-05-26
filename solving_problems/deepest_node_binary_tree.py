
"""
Input : below tree
      1
    /   \
   2      3
  / \    / \
 4   5  6   7
           / \
          8   9


or a serialization of the given tree:
[1,2,3,4,5,6,7,"","","","","","",8,9]

Output : 9

Input : below tree
            1
          /   \
         2      3
               /
              6
Output : 6

Given a binary tree, find the deep­est node in it.
"""

# Utility function for a node creation


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.seen = False


# Solution1
"""
Inorder traversal of a given binary tree, keep track of maximum level and deepest node
seen so far.
Time complexity O(n).
"""


def find(root, level, maxLevel, res):

    if (root != None):
        level += 1
        find(root.left, level, maxLevel, res)

        # Update level and result
        if (level > maxLevel[0]):
            res[0] = root.data
            maxLevel[0] = level

        find(root.right, level, maxLevel, res)

# Returns value of deepest node


def deepestNode(root):

    # Initialze result and max level
    res = [-1]
    maxLevel = [-1]

    # Update "res" and "maxLevel"
    # Note that res and maxLevel are passed
    # by reference.
    find(root, 0, maxLevel, res)
    return res[0]


# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.right.left = newNode(8)
    root.right.right.right = newNode(9)
    print(
        f"Solution #1 recursively found the deepest node as: {deepestNode(root)}")

# Solution 2
"""
Find the height of the given tree, use it as a counter to traverse
from the root to the corresponding level of the deepest node, 
and then print the node at the bottom-most level.
Time complexity: O(n)
"""

# Utility function to find a height
# of a tree, rooted at 'root'.


def height(root):
    if(not root):
        return 0

    leftHt = height(root.left)
    rightHt = height(root.right)

    return max(leftHt, rightHt) + 1


"""
or 'shorthand' version:

def heigh(root):
    return max(height(root.left), height(root.right))+1 if root else 0
    
"""

# levels : current Level
# Utility function to print all
# nodes at a given level.


def deepestNodes2(root, levels):
    if(not root):
        return

    if(levels == 1):
        print(root.data)
    elif(levels > 1):
        deepestNodes2(root.left, levels - 1)
        deepestNodes2(root.right, levels - 1)


# Driver Code
if __name__ == '__main__':
    # Calculating height of tree
    levels = height(root)
    # Printing the deepest node
    print("Solution #2 due to the level counter recursively found the deepest nodes")
    deepestNodes2(root, levels)


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
            return self.items[-1].data  # peek the last item

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


def subtreeWithAllDeepest(root):
    def deep(root):
        if not root:
            return 0, None
        l, r = deep(root.left), deep(root.right)
        if l[0] > r[0]:
            return l[0] + 1, l[1]
        elif l[0] < r[0]:
            return r[0] + 1, r[1]
        else:
            return l[0] + 1, root
    return deep(root)[1]

# utility function for printing array representation of a binary tree


def print_tree_levelorder(start):
    if start is None:
        return

    queue = Queue()
    queue.enqueue(start)

    array = []
    while len(queue) > 0:
        array.append(queue.peek())
        node = queue.dequeue()

        if node.left:
            queue.enqueue(node.left)
        if not node.left and node.right:
            array.append("")
        if node.right:
            queue.enqueue(node.right)

    return array


# Driver Code
if __name__ == '__main__':
    # Printing the deepest subtree
    print(
        f"Subtree with the all deepest nodes found: {print_tree_levelorder(subtreeWithAllDeepest(root))}")
