# Write a function that takes a head node and an integer value n and then returns the nth to last
# node in the linked list.
from typing import Any

class Node:

    def __init__(self, value: Any) -> None:
        
        self.value = value
        self.nextnode = None

def nth_to_last_node(n: int, head: Node) -> Node:
    
    curr_node = head
    num_nodes = 1

    # Find total number of nodes
    while curr_node.nextnode:
        num_nodes += 1
        curr_node = curr_node.nextnode
    
    # Find target node based on total number of nodes and n
    curr_node_ind = 1
    target_node_ind = num_nodes - n + 1
    curr_node = head

    # Move to target node
    while curr_node_ind != target_node_ind:
        curr_node = curr_node.nextnode
        curr_node_ind += 1

    return curr_node

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

target_node = nth_to_last_node(2, a)

print(target_node.value)

def nth_to_last_node2(n: int, head: Node) -> Node:
    
    left_pointer = head
    right_pointer = head

    # Establishes block n number of nodes wide
    # E.g. ( [A|-]-> [B|-]-> ) [C|-]-> [D|-]-> [E|-]-> None
    for i in range(n -1):

        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than linked list')
        
        right_pointer = right_pointer.nextnode

    # Move both boundaries of the block (pointers) simultaneously until the block reaches end of linked list
    # E.g. [A|-]-> [B|-]-> [C|-]-> ( [D|-]-> [E|-]-> ) None
    while right_pointer.nextnode:

        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    # Left pointer will be nth to last node
    return left_pointer

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

target_node = nth_to_last_node2(2, a)

print(target_node.value)