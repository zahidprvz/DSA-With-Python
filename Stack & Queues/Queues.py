class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queues:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.lenght = 1

    def print_queue(self):
        temp = self.first
        while(temp):
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.lenght += 1
        

    def dequeue(self):
        if self.lenght == 0:
            return None
        temp = self.first
        if self.lenght == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.lenght -= 1
        return temp 

my_queues = Queues(143)
my_queues.enqueue(108)
my_queues.enqueue(35)

print("Initial Queue: ")
my_queues.print_queue()

print("\n\nQueue after dequeuing an element: ")
my_queues.dequeue()
my_queues.print_queue()