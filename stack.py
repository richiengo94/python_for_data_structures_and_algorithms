# Stacks follow last-in-first-out LIFO restrictions
# in -> 1, 2, 3, 4, out -> 4, 3, 2, 1

from typing import Any

class Stack(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def push(self, item: Any) -> None:

        self.items.append(item)

    def pop(self) -> Any:

        return self.items.pop()
    
    def peek(self) -> Any:

        return self.items[-1]
    
    def size(self) -> int:

        return len(self.items)
    
s = Stack()

print(s.isEmpty())

s.push(1)
s.push('two')

print(s.peek())

s.push(True)

print(s.size())

print(s.isEmpty())

for i in range(3):
    print(s.pop())

print(s.isEmpty())