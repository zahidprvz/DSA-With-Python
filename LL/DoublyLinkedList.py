class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Prints all values in the linked list."""
        if self.length == 0:
            print("There are no elements in LL")
            return
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    # ==========================
    # Core Operations
    # ==========================
    def append(self, value):
        """Adds a node with the given value to the end of the linked list."""
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Removes and returns the last node from the doubly linked list."""
        if self.head is None:  # Case: Empty list
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.tail = None
        self.length -= 1
        return temp

my_d_ll = DoublyLinkedList(1)
my_d_ll.append(2)
my_d_ll.append(3)
my_d_ll.append(4)
my_d_ll.append(5)
my_d_ll.print_list()
print(my_d_ll.pop())
