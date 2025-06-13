# Given a singly linked list, write a function which takes in the first node in a singly linked list
# and return a boolean indicating if the linked list conatins a "cycle".
# A cycle is when a node's next point actually points back to a previous node in the list. This is
# also sometimes known as a circularly linked list.

from typing import Any

class Node(object):

    def __init__(self, value: Any) -> None:
        
        self.value = value
        self.next_node = None

def cycle_check(node: Node) -> bool:
    