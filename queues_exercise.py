from typing import Any

class Queue(object):
    """Class for queues"""

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:
        """Returns boolean to check if queue is empty"""

        return self.items == []

    def enqueue(self, item: Any) -> None:
        """Adds/enqueues item to rear of queue"""

        self.items.insert(0 , item)

    def dequeue(self) -> Any:
        """Removes and returns/dequeues item at front of queue"""

        return self.items.pop()
    
    def size(self) -> int:
        """Return size of queue"""

        return len(self.items)

q = Queue()

print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())

class Queue2(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def enqueue(self, item: Any) -> None:

        self.items.insert(0, item)

    def dequeue(self) -> Any:

        return self.items.pop()
    
    def size(self) -> int:

        return len(self.items)

q = Queue2()

print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())

class Queue3(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def enqueue(self, item: Any) -> None:

        self.items.insert(0, item)

    def dequeue(self) -> Any:

        return self.items.pop()
    
    def size(self) -> int:

        return len(self.items)

q = Queue3()

print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())

class Queue4(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def enqueue(self, item: Any) -> None:

        self.items.insert(0, item)

    def dequeue(self) -> Any:

        return self.items.pop()
    
    def size(self) -> int:

        return len(self.items)

q = Queue4()

print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())

class Queue5(object):

    def __init__(self) -> None:
         
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def enqueue(self, item: Any) -> None:

        self.items.insert(0, item)

    def dequeue(self) -> Any:

        return self.items.pop()
    
    def size(self) -> int:

        return len(self.items)

q = Queue5()

print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())

class Queue6(object):

    def __init__(self) -> None:
        
        self.items = []

    def isEmpty(self) -> bool:

        return self.items == []
    
    def enqueue(self, item: Any) -> None:

        self.items.insert(0, item)

    def dequeue(self) -> Any:

        return self.items.pop()
    
    def size(self) -> int:

        return len(self.items)

q = Queue6()

print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())