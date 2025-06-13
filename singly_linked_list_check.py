# Given a singly linked list, write a function which takes in the first node in a singly linked list
# and return a boolean indicating if the linked list conatins a "cycle".
# A cycle is when a node's next point actually points back to a previous node in the list. This is
# also sometimes known as a circularly linked list.

from typing import Any

class Node(object):

    def __init__(self, value: Any) -> None:
        
        self.value = value
        self.next_node = None

# Not a robust method
def cycle_check(node: Node) -> bool:

        start_node = node
        current_node = start_node.next_node

        # Should break out of while loop if it hits non-cycling tail and returns False
        while current_node.next_node is not None:

            # If it cycles through whole list, the current node and the start node will end up being the same and return True
            # This only assumes that it cycles through the WHOLE linked list (i.e. it would have to pass through the start node again)
            # This doesn't work if for some reason the linked list is only partially circular (e.g. a -> b -> c -> b)
            if current_node == start_node:
                 return True
            
            current_node = current_node.next_node

        return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a

print(cycle_check(a))

x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z

print(cycle_check(x))

# This avoids the assumption in cycle_check()
def cycle_check2(node: Node) -> bool:
     
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:
        
        # Since they traverse at different rates, at some point, the markers will eventually be the same assuming it is a circularly linked list
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = b

print(cycle_check2(a))