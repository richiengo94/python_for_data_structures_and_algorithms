# Deque (double-ended queue) can have items added or remove from either ends of the deque
from typing import Any

class Deque(object):

    def __init__(self) -> None:
        
        self.items = []

    def addFront(self, item: Any) -> None:

        self.items.append(item)

    def addRear(self, item: Any) -> None:

        self.items.insert(0, item)

    def removeFront(self) -> Any:

        return self.items.pop()

    def removeRear(self) -> Any:

        return self.items.pop(0)

    def isEmpty(self) -> bool:

        return self.items == []
    
    def size(self) -> int:

        return len(self.items)
    
d = Deque()

d.addFront('hello')
d.addRear('world')

print(d.size())

print(d.removeFront() + ' ' + d.removeRear())

print(d.size())
print(d.isEmpty())