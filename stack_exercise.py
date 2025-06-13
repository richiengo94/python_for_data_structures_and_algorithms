from typing import Any

class Stack(object):
    """Class for stack"""

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:
        """Returns boolean to check if stack is empty"""
        return self.items == []
    
    def push(self, item: Any) -> None:
        """Adds/pushes item to the end/top of the stack"""
        self.items.append(item)

    def pop(self) -> Any:
        """Removes and returns/pops item at end/top of the stack"""
        return self.items.pop()

    def peek(self) -> Any:
        """Returns item at end/top of the stack without removing it"""
        return self.items[-1]
    
    def size(self) -> int:
        """Returns size of the stack"""
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
    
class Stack2(object):

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
    
s = Stack2()

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
    
class Stack3(object):

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
    
s = Stack3()

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

class Stack4(object):

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
    
s = Stack4()

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

class Stack5(object):

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

s = Stack5()

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

class Stack6(object):

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

s = Stack6()

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
