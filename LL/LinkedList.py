# ==========================
# LinkedList Implementation
# ==========================

class Node:
    """Node class to represent each element in the LinkedList."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """LinkedList class with various methods for linked list operations."""

    # ==========================
    # Constructor and Utilities
    # ==========================
    def __init__(self, value):
        """
        Initializes the linked list with a single node.

        Args:
            value: The initial value for the linked list.
        """
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        return True

    def pop(self):
        """Removes and returns the last node from the linked list."""
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """Adds a node with the given value to the beginning of the linked list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True 

    def pop_first(self):
        """Removes and returns the first node from the linked list."""
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    # ==========================
    # Index-based Operations
    # ==========================
    def get(self, index):
        """Returns the node at the given index."""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(0, index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """Sets the value of the node at the given index."""
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Inserts a node at the given index."""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """Removes the node at the given index."""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()

        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None 
        self.length -= 1
        return temp

    # ==========================
    # Advanced Features
    # ==========================
    def reverse(self):
        """Reverses the linked list in place."""
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle(self):
        """Finds and returns the middle node of the linked list."""
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.value

    def has_loop(self):
        """Checks if the linked list contains a loop."""
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        """Removes duplicate values from the linked list."""
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

    def kth_element(self, ll, k):
        """finds the kth element from the linked list."""
        slow = fast = self.head
        if k == 0:
            return None
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.value

    def reverse_between(self, m, n):
        if not self.head:
            return None
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(m):
            prev = prev.next

        current = prev.next
        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        self.head = dummy.next


my_ll = LinkedList(11)
my_ll.append(23)
my_ll.append(3)
my_ll.append(9)
my_ll.append(10)
my_ll.append(11)


print("Before Setting value")
my_ll.print_list()
my_ll.set_value(3, 1)
print("After Setting value")
my_ll.print_list()
my_ll.insert(2, 1000)
print("Now after inserting 1000 at the 3rd index: ")
my_ll.print_list()
print("Now After removing value at 2nd index")
my_ll.remove(2)
my_ll.print_list()
print("Now this is reversed LL: ")
my_ll.reverse()
my_ll.print_list()
print("Middle node in LL: ", my_ll.find_middle())
print("After removing the duplicants: ", my_ll.remove_duplicates())
my_ll.print_list()
# print("Element at 6th index: " + str(my_ll.get(6)))
print("Kth element from end in LL: ")
print(my_ll.kth_element(my_ll, 4))