# Double linked lists have nodes that reference node before and after
# Greater variety of O(1) time update operations including insertions and deletions
# "Next" node refers to node after, "prev" node refers to node before
# Special nodes at ends: header node at beginning of list, trailer node at end of list
# Special nodes at ends referred to as sentinels (or guards)

# header [| |<->] [<->|JFK|<->] [<->|PVD|<->] [<->|SFO|<->] [<->| |] trailer

# Every insertion into DLL occurs between a pair of nodes (nothing goes before header or after trailer)

from typing import Any

class DoublyLinkedListNode(object):

    def __init__(self, value: Any):
        
        self.value = value
        self.next_node = None
        self.prev_node = None
    
a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next_node = b
b.next_node = c
c.prev_node = b
b.prev_node = a