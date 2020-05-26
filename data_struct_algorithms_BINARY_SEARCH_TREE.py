"""
BST are sorted trees - every value on the left of a particular node is smaller than it
and every value on the right of a particular node is larger than it
Unbalanced BST: The distribution of nodes is skewed to the right side
Worst case: linear time O(n)
Average case: O(log(n))

Now try implementing a BST on your own.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, curr, new_val):
        if curr.value < new_val:
            if curr.right:
                return self.insert_helper(curr.right, new_val)
            else:
                curr.right = Node(new_val)
        else:
            if curr.left:
                return self.insert_helper(curr.left, new_val)
            else:
                curr.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, curr, find_val):
        if curr:
            if find_val == curr.value:
                return True
            elif find_val < curr.value:
                return self.search_helper(curr.left, find_val)
            else:
                return self.search_helper(curr.right, find_val)
        return False


        # Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
