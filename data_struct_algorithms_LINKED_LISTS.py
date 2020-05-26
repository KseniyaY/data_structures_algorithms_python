class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class linked_list:
    def __init__(self, head=None):
        self.head = node(head)

    # Adds new node to the end of the linked list.
    def append(self, new_node):
        new_node = node(new_node)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Adds new node at front of the linked list.
    def add_at_front(self, new_node):
        new_node = node(new_node)
        new_node.next = self.head
        self.head = new_node

    # Insert new node at the indicated position
    def insert_at_position(self, new_node, position):
        new_node = node(new_node)
        counter = 0
        current = self.head
        if position > 0:
            while current and counter < position:
                if counter == position - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                counter += 1
        elif position == 0:
            new_node.next = self.head
            self.head = new_node

    # Returns the length (integer) of the linked list.

    def length(self):
        current = self.head
        total_length = 0
        while current.next:
            total_length += 1
            current = current.next
        return total_length

    # Prints out the linked list in traditional Python list format.
    def display(self):
        elems = []
        current = self.head
        delimiter = " => "
        while current.next:
            elems.append(str(current.value))
            current = current.next
        print(delimiter.join(elems))

    # Returns the value of the node at 'position'.
    def get_at_position(self, position):
        if position >= self.length() or position < 0:  # position<0
            print("ERROR: 'get_at_position' - Position out of range!")
            return
        counter = 0
        current = self.head
        while current and counter <= position:
            if counter == position:
                print(current.value)
                return current
            counter += 1
            current = current.next

    # Delete the first node with a given value
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    # Delete the first node
    def delete_first(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted

    # Deletes the node at a certain position 'position'
    def delete_at_position(self, position):
        if position >= self.length() or position < 0:  # added 'position<0' post-video
            print("ERROR: 'delete_by_position' Index out of range!")
            return
        counter = 0
        current = self.head
        while True:
            previous = current
            current = current.next
            if counter == position:
                previous.next = current.next
                return
            counter += 1

    # Sets the new_node at position equal to 'new_node'.
    # Position begin at 0. If the position is greater than or equal
    # to the length of the linked list a warning will be printed
    # to the user.
    def set_new_value(self, position, value):
        if position >= self.length() or position < 0:
            print("ERROR: 'set_new_value' - Index out of range!")
            return
        current = self.head
        counter = 0
        while True:
            if counter == position:
                current.value = value
                return
            current = current.next
            counter += 1


my_list = linked_list(0)
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.display()
my_list.set_new_value(3, 33)
my_list.display()
my_list.insert_at_position(78, 4)
my_list.insert_at_position(79, 0)
my_list.display()
my_list.delete(33)
my_list.delete_at_position(0)
my_list.display()
my_list.add_at_front(11)
my_list.get_at_position(1)
my_list.display()
my_list.delete_first()
my_list.display()
