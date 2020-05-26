"""Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Algorithm
 
The algorithm for this question is quite simple since the two linked lists are already sorted. 
We create a new linked list and loop through both lists appending the smaller nodes.

(1) Create a new head pointer to an empty linked list.
(2) Check the first value of both linked lists.
(3) Whichever node from L1 or L2 is smaller, append it to the new list and
move the pointer to the next node.
(4) Continue this process until you reach the end of a linked list.

Example

L1 = 1 -> 3 -> 10
L2 = 5 -> 6 -> 9
L3 = null

Compare the first two nodes in both linked lists: (1, 5), 1 is smaller 
so add it to the new linked list and move the pointer in L1.
L1 = 3 -> 10
L2 = 5 -> 6 -> 9
L3 = 1

Compare the first two nodes in both linked lists: (3, 5), 3 is smaller 
so add it to the new linked list and move the pointer in L1.
L1 = 10
L2 = 5 -> 6 -> 9
L3 = 1 -> 3

Compare the first two nodes in both linked lists: (10, 5), 5 is smaller 
so add it to the new linked list and move the pointer in L2.
L1 = 10
L2 = 6 -> 9
L3 = 1 -> 3 -> 5

Compare the first two nodes in both linked lists: (10, 6), 6 is smaller 
so add it to the new linked list and move the pointer in L2.
L1 = 10
L2 = 9
L3 = 1 -> 3 -> 5 -> 6

Compare the first two nodes in both linked lists: (10, 9), 9 is smaller 
so add it to the new linked list and move the pointer in L2.
L1 = 10
L2 = null
L3 = 1 -> 3 -> 5 -> 6 -> 9

Because L2 points to null, simply append the rest of the nodes
from L1 and we have our merged linked list.
L3 = 1 -> 3 -> 5 -> 6 -> 9 -> 10
"""

# Definition for singly-linked list.


class ListNode():
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

# Prints out the linked list in traditional Python list format.


def display(linked_list):
    elems = []
    current = linked_list
    delimiter = " => "
    while current.next:
        elems.append(str(current.val))
        current = current.next
    print(delimiter.join(elems))

# Approach 1: Recursive merge


class Recursive_solution():
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head


# create first linked list: 1 -> 3 -> 10
n3 = ListNode(10)
n2 = ListNode(3, n3)
n1 = ListNode(1, n2)
L1 = n1

# create second linked list: 5 -> 6 -> 9
n6 = ListNode(9)
n5 = ListNode(6, n6)
n4 = ListNode(3, n5)
L2 = n4


pyRecursiveSolution = Recursive_solution()
l3 = pyRecursiveSolution.mergeTwoLists(L1, L2)
display(l3)


# Approach 2: Iterative merge


class Iterative_solution():
    def mergeTwoLists(self, l1, l2):
        self.head = tail = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                # move the pointer to the next node replacing l1
                # with the next value for looping
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                # move to the pointer to the next node replacing l2
                # with the next value for looping
            tail = tail.next

        # connect the tail with the last remaining node
        tail.next = l1 or l2
        return self.head.next


# create first linked list: 1 -> 3 -> 10
node3 = ListNode(10)
node2 = ListNode(3, node3)
node1 = ListNode(1, node2)
L1 = node1

# create second linked list: 5 -> 6 -> 9
node6 = ListNode(9)
node5 = ListNode(6, node6)
node4 = ListNode(3, node5)
L2 = node4

pyIterativeSolution = Iterative_solution()
l4 = pyIterativeSolution.mergeTwoLists(L1, L2)
display(l4)

"""
Complexity Analysis
Time complexity: this algorithm runs in O(n + m) time where n and m are the lengths of the respective linked lists. 
This is the linear run time because to merge both linked lists into one, we need to iterate through each node in the list.
"""
