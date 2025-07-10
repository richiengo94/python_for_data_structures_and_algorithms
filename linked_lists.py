from typing import Any

class SinglyLinkedList(object):

    def __init__(self, value: Any):
        self.value = value
        self.next_node = None

class DoublyLinkedList(object):

    def __init__(self, value: Any):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = SinglyLinkedList(1)
b = SinglyLinkedList(2)
c = SinglyLinkedList(3)

a.next_node = b
b.next_node = c

x = DoublyLinkedList(1)
y = DoublyLinkedList(2)
z = DoublyLinkedList(3)

x.next_node = y
y.prev_node = x
y.next_node = z
z.prev_node = y

class SinglyLinkedList1(object):

    def __init__(self, value: Any):
        self.value = value
        self.next_node = None

class DoublyLinkedList1(object):

    def __init__(self, value: Any):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = SinglyLinkedList1(1)
b = SinglyLinkedList1(2)
c = SinglyLinkedList1(3)

a.next_node = b
b.next_node = c

x = DoublyLinkedList1(1)
y = DoublyLinkedList1(2)
z = DoublyLinkedList1(3)

x.next_node = y
y.prev_node = x
y.next_node = z
z.prev_node = y
