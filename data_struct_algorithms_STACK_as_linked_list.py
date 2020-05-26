class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node()
        new_node.data = data
        next_node = self.head
        self.head = new_node
        self.head.next = next_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            head_node = self.head
            self.head = self.head.next
            self.size -= 1
            return head_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def stack_size(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def __str__(self):
        returned_str = ''
        current_node = self.head
        while current_node:
            returned_str += str(current_node.data + " ")
            current_node = current_node.next
        return returned_str


class Node:
    def __init__(self):
        self.data = None
        self.next = None


if __name__ == "__main__":
    # it is done so that this code launches being called solely
    # via the python command in terminal,
    # like "python Stack_as_linked_list.py"
    test_stack = Stack()
    test_stack.push("a")
    test_stack.push("b")
    test_stack.push("c")
    print(test_stack.stack_size())
    print(test_stack)
    print(test_stack.peek())
    first_item = test_stack.pop()
    print("popped " + str(first_item))
    print(test_stack.is_empty())
    print(test_stack.stack_size())
    print(test_stack)
