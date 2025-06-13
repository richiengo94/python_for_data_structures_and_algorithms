from typing import Any

class Queue2Stacks(object):
    """Class to implement queue from two stacks"""
    def __init__(self) -> None:
        
        self.stack1 = []
        self.stack2 = [] # uses stack 2 as the queue

    def enqueue(self, element: Any) -> None:
        """Method to add to queue using 2 stacks"""
        
        if self.stack2 == []:
            # if stack 2 is empty, just add straight in as first element
            self.stack2.append(element) 
        else:
            for i in range(len(self.stack2)):
                #  move everything from stack2 to stack 1 in LIFO order
                self.stack1.append(self.stack2.pop())

            # add the new element as first element (end of) stack2
            self.stack2.append(element)

            # move everything back from stack1 to stack in FIFO order
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

    def dequeue(self) -> Any:
        """Method to remove from queue using 2 stacks"""

        return self.stack2.pop()
        

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())

class Queue2Stacks2(object):

    def __init__(self) -> None:
        
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element: Any) -> None:
        # Just stuff everything into stack1 for enqueue
        self.stack1.append(element)

    def dequeue(self) -> Any:
        # Since dequeue *shouldn't* be called when there's nothing in stack1, stack1 starts in LIFO order
        # Nothing is moved from stack1 to stack2 until stack2 is empty, so nothing will be out of order
        if not self.stack2:
            # If stack2 is empty, move everything from stack1 to stack2 in FIFO order
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Even if enqueue is called while there is stuff in stack2, stack2 will still output FIFO order until it gets emptied
        return self.stack2.pop()

q = Queue2Stacks2()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())

class Queue2Stacks3(object):

    def __init__(self):
        
        self.instack = []
        self.outstack = []

    def enqueue(self, item: Any) -> None:

        self.instack.append(item)

    def dequeue(self) -> Any:

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        
        return self.outstack.pop()

q = Queue2Stacks3()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())