"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

or

input:
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
[[1],[2,3],[4,5,6,7],[8,9]]
or
[[A],[B,C],[D,E,F,G]]
"""


# utility function for node creation


from collections import deque


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

# Solution #1 (recursive)


def levelOrder(root):
    if not root:
        return []

    answer = []
    traverse(root, 1, answer)
    return answer


def traverse(node, level, answer):
    if not node:
        return

    if level > len(answer):
        # we are at a new level
        answer.append([node.data])
    else:
        answer[level-1].extend([node.data])

    traverse(node.left, level + 1, answer)
    traverse(node.right, level + 1, answer)


# Solution #2 (queue)
def levelOrder2(root):
    if not root:
        return []
    queue, res = deque([root]), []

    while queue:
        cur_level, size = [], len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            cur_level.append(node.data)
        res.append(cur_level)
    return res


# Solution #3
"""
Breadh First Search

Using BFS, at any instant only L1 and L1+1 nodes are in the queue.
When we start the while loop, we have L1 nodes in the queue.
for _ in range(len(q)) allows us to dequeue L1 nodes one by one and add L2 children one by one.
Time complexity: O(N). Space Complexity: O(N)
"""


def levelOrder3(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    q, result = deque(), []
    if root:
        q.append(root)
    while len(q):
        level = []
        for _ in range(len(q)):
            x = q.popleft()
            level.append(x.data)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        result.append(level)
    return result


# Solution #4 DFS
"""
Depth First Search

Use a variable to track level in the tree and use simple Pre-Order traversal
Add sub-lists to result as we move down the levels
Time Complexity: O(N)
Space Complexity: O(N) + O(h) for stack space
"""


def levelOrder4(root):
    result = []
    helper(root, 0, result)
    return result


def helper(root, level, result):
    if root is None:
        return
    if len(result) <= level:
        result.append([])
    result[level].append(root.data)
    helper(root.left, level+1, result)
    helper(root.right, level+1, result)


if __name__ == '__main__':
    print(f"Solution #1 recursive: {levelOrder(root)}")
   # [[1], [2, 3], [4, 5, 6, 7], [8, 9]]
    print(f"Solution #2 queue: {levelOrder2(root)}")
    # [[1], [2, 3], [4, 5, 6, 7], [8, 9]]
    print(f"Solution #3 BFS: {levelOrder3(root)}")
    # [[1], [2, 3], [4, 5, 6, 7], [8, 9]]
    print(f"Solution #4 DFS: {levelOrder4(root)}")
    # [[1], [2, 3], [4, 5, 6, 7], [8, 9]]
