#Doubly_linked_list
"""
class Node:
    def __init__(self, value):  # Corrected __init__
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):  # Corrected __init__
        self.start = None
        self.end = None

    def add(self, number):
        new_node = Node(number)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def show(self):
        current = self.start
        while current:
            print(current.value)
            current = current.next

table_list = LinkedList()
a = int(input("Enter a number (a): "))
b = int(input("Enter another number (b): "))

if a == 0 and b == 0:
    print("Both numbers are zero")
else:
    c = a // b
    table_list.add(c)
    print(" division: ", c)
    table_list.show()
"""
''''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class Doublylinkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.next = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return True
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail.prev = self.tail
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:  # Note: changed > to >=
            return None
        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp  # ✅ return the Node object itself

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
          temp.value = value
          return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp.value



my_doublylinkedlist = Doublylinkedlist(1)
my_doublylinkedlist.append(2)
my_doublylinkedlist.append(3)
my_doublylinkedlist.append(4)
my_doublylinkedlist.append(5)
#my_doublylinkedlist.prepend(1)

#print(my_doublylinkedlist.pop_first())
#print(my_doublylinkedlist.pop())
#print(my_doublylinkedlist.get(3))
#my_doublylinkedlist.set_value(2, 4)

#my_doublylinkedlist.insert(1, 2)
my_doublylinkedlist.remove(1)
my_doublylinkedlist.print_list()
'''

#Stacks
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.next = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def push_stack(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value

my_stack = Stack(4)
my_stack.push_stack(3)
my_stack.push_stack(5)
my_stack.push_stack(6)
print(my_stack.pop(), '/n')
my_stack.print_stack()
'''

'''
#queue:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.start = new_node
        self.end = new_node
        self.length = 1

    def print_que(self):
        temp = self.start
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node
        self.length += 1

    def dequeue(self):
        temp = self.start
        if self.length == 0:
            return None
        elif self.length == 1:
            self.start = None
            self.end = None
        else:
            self.start = self.start.next
            temp.next = None
        self.length -= 1
        return temp.value

my_que = Queue(1)
my_que.enqueue(2)

print(my_que.dequeue())
print(my_que.dequeue())
print(my_que.dequeue())
'''

