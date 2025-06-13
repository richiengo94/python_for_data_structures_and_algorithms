# Singly linked list is collection of nodes in a linear sequence
# Each node contains reference to element of sequence and reference to next node assuming it is not the tail (end node)
# Nothing points to head (first node)
# Tail points to None as next node
# Moving through nodes and linked list is traversing
# Linked list does not have a predetermined fixed size and is proportional to # of elements

# [MSP|-]-> [ATL|-]-> [BOS|-]-> None, MSP is head, BOS is tail

# Cannot easily delete the last node of a linked list
# Constant O(1) insertion and deletion
# O(k) time to reach k-th node

from typing import Any

class Node(object):

    def __init__(self, value: Any):
        
        self.value = value
        self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

print(a.value)
print(a.next_node.value)