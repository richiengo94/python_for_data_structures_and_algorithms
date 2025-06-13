# Write a function to reverse a Linked List in place. The function will take in the head of the list as
# input and return the new head of the list.

from typing import Any

class Node(object):

    def __init__(self, value: Any) -> None:
        
        self.value = value
        self.next_node = None

def reverse(head: Node) -> Node:

    rev_node = [None]
    
    curr_node = head

    while curr_node.next_node:
        rev_node.append(curr_node)
        curr_node = curr_node.next_node

    new_head = curr_node

    while len(rev_node) > 0:
        curr_node.next_node = rev_node.pop()
        curr_node = curr_node.next_node

    return new_head

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d

print(a.next_node.value)
print(b.next_node.value)
print(c.next_node.value)

print(reverse(a).value)
print(d.next_node.value)
print(c.next_node.value)
print(b.next_node.value)

def reverse2(head: Node) -> Node:

    current = head
    previous = None
    next_node = None

    while current:

        next_node = current.next_node

        current.next_node = previous

        previous = current
        current = next_node

    return previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d

print(a.next_node.value)
print(b.next_node.value)
print(c.next_node.value)

print(reverse2(a).value)
print(d.next_node.value)
print(c.next_node.value)
print(b.next_node.value)