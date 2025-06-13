# Queue added to rear (enqueue) and pulled from front (dequeue). 
# Follows first-in-first-out FIFO restrictions
# in -> 1, 2, 3, 4, out -> 1, 2, 3, 4

from typing import Any

class Queue(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:
        
        return self.items == []
    
    def enqueue(self, item: Any) -> None:

        self.items.insert(0 , item)

    def dequeue(self) -> Any:

        return self.items.pop()
    
    def size(self) -> int:

        return len(self.items)
    
q = Queue()

print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())