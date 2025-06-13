from typing import Any

class Deque(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def addFront(self, item: Any) -> None:

        self.items.append(item)

    def addRear(self, item: Any) -> None:

        self.items.insert(0, item)

    def removeFront(self) -> Any:

        return self.items.pop()
    
    def removeRear(self) -> Any:

        return self.items.pop(0)
    
    def size(self) -> int:

        return len(self.items)

d = Deque()

d.addFront('hello')
d.addRear('world')

print(d.size())

print(d.removeFront() + ' ' + d.removeRear())

print(d.size())
print(d.isEmpty())

class Deque2(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def addFront(self, item: Any) -> None:

        self.items.append(item)

    def addRear(self, item: Any) -> None:

        self.items.insert(0, item)

    def removeFront(self) -> Any:

        return self.items.pop()
    
    def removeRear(self) -> Any:

        return self.items.pop(0)
    
    def size(self) -> int:

        return len(self.items)

d = Deque2()

d.addFront('hello')
d.addRear('world')

print(d.size())

print(d.removeFront() + ' ' + d.removeRear())

print(d.size())
print(d.isEmpty())

class Deque3(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def addFront(self, item: Any) -> None:

        self.items.append(item)
    
    def addRear(self, item: Any) -> None:

        self.items.insert(0, item)

    def removeFront(self) -> Any:

        return self.items.pop()
    
    def removeRear(self) -> Any:

        return self.items.pop(0)
    
    def size(self) -> int:

        return len(self.items)

d = Deque3()

d.addFront('hello')
d.addRear('world')

print(d.size())

print(d.removeFront() + ' ' + d.removeRear())

print(d.size())
print(d.isEmpty())

class Deque4(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def addFront(self, item: Any) -> None:

        self.items.append(item)

    def addRear(self, item: Any) -> None:

        self.items.insert(0, item)

    def removeFront(self) -> Any:

        return self.items.pop()
    
    def removeRear(self) -> Any:

        return self.items.pop(0)
    
    def size(self) -> int:

        return len(self.items)

d = Deque4()

d.addFront('hello')
d.addRear('world')

print(d.size())

print(d.removeFront() + ' ' + d.removeRear())

print(d.size())
print(d.isEmpty())

class Deque5(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def addFront(self, item: Any) -> None:

        self.items.append(item)

    def addRear(self, item: Any) -> None:

        self.items.insert(0, item)

    def removeFront(self) -> Any:

        return self.items.pop()
    
    def removeRear(self) -> Any:

        return self.items.pop(0)
    
    def size(self) -> int:

        return len(self.items)

d = Deque5()

d.addFront('hello')
d.addRear('world')

print(d.size())

print(d.removeFront() + ' ' + d.removeRear())

print(d.size())
print(d.isEmpty())

class Deque6(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def addFront(self, item: Any) -> None:

        self.items.append(item)

    def addRear(self, item: Any) -> None:

        self.items.insert(0, item)

    def removeFront(self) -> Any:

        return self.items.pop()
    
    def removeRear(self) -> Any:

        return self.items.pop(0)
    
    def size(self) -> int:

        return len(self.items)

d = Deque6()

d.addFront('hello')
d.addRear('world')

print(d.size())

print(d.removeFront() + ' ' + d.removeRear())

print(d.size())
print(d.isEmpty())