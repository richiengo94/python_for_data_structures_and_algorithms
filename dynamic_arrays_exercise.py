# Dynamic array exercise

import ctypes
from typing import Any

class DynamicArray(object): # inherits object class
    """Class for dynamic arrays"""

    def __init__(self) -> None:

        self.n = 0 # number of elements
        self.capacity = 1
        self.A = self.make_array(self.capacity) # A-array from lecture

    def __len__(self) -> int:
        """Returns number of elements (length) of self"""
        return self.n
    
    def __getitem__(self, k: int):
        """Return the element at index k"""

        if not (0 <= k <= self.n):
            return IndexError('K is out of bounds!')
        
        return self.A[k]
    
    def append(self, ele: Any) -> None:
        """Appends element to array"""

        if self.n == self.capacity:
            self._resize(2 * self.capacity) # Doubles capacity if capacity is full; main point

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap: int) -> None:
        """Resizes array by creating new array with larger capacity, moving new elements to
         new array, then setting to original array"""
        B = self.make_array(new_cap) 

        for k in range(self.n):
            B[k] = self.A[k] # B-array from lecture

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap: int):
        """Creates new array with larger capacity"""
        return (new_cap * ctypes.py_object)()
    
arr = DynamicArray()
print("DynamicArray")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A)}")

class DynamicArray1(object):

    def __init__(self) -> None:

        self.num_elements = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self) -> int:

        return self.num_elements

    def __getitem__(self, k) -> Any:

        return self.A[k]

    def append(self, element: Any) -> None:

        if self.num_elements == self.capacity:
            self._resize(2 * self.capacity)
        
        self.A_array[self.num_elements] = element
        self.num_elements += 1

    def _resize(self, new_cap) -> None:
        
        B_array = self.make_array(new_cap)

        for i in range(self.num_elements):
            B_array[i] = self.A_array[i]

        self.A_array = B_array
        self.capacity = new_cap

    def make_array(self, new_cap: int):

        return (new_cap * ctypes.py_object)()
    
arr = DynamicArray1()
print("DynamicArray 1")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A_array)}")

class DynamicArray2(object):

    def __init__(self) -> None:
        
        self.num_elements = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self) -> int:

        return self.num_elements
    
    def __getitem__(self, k: int) -> Any:

        return self.A_array[k]
    
    def append(self, element: Any) -> None:

        if self.num_elements == self.capacity:
            self._resize(2 * self.capacity)

        self.A_array[self.num_elements] = element
        self.num_elements += 1

    def _resize(self, new_cap: int) -> None:
        
        B_array = self.make_array(new_cap)

        for i in range(self.num_elements):
            B_array[i] = self.A_array[i]

        self.A_array = B_array
        self.capacity = new_cap

    def make_array(self, new_cap: int):
        
        return (new_cap * ctypes.py_object)()
    
arr = DynamicArray2()
print("DynamicArray 2")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A_array)}")


class DynamicArray3(object):

    def __init__(self):
        
        self.num_elements = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self) -> int:

        return self.num_elements
    
    def __getitem__(self, k: int) -> Any:

        return self.A_array[k]
    
    def append(self, element: Any) -> None:

        if self.num_elements == self.capacity:
            self._resize(2 * self.capacity)

        self.A_array[self.num_elements] = element
        self.num_elements += 1

    def _resize(self, new_cap: int) -> None:

        B_array = self.make_array(new_cap)

        for i in range(self.num_elements):
            B_array[i] = self.A_array[i]

        self.A_array = B_array
        self.capacity = new_cap

    def make_array(self, new_cap: int):

        return (new_cap * ctypes.py_object)()

arr = DynamicArray3()
print("DynamicArray 3")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A_array)}")

class DynamicArray4(object):
    
    def __init__(self):
        
        self.num_elements = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self) -> int:
        
        return self.num_elements

    def __getitem__(self, k: int) -> Any:
        
        return self.A_array[k]

    def append(self, element: Any) -> None:
        
        if self.num_elements == self.capacity:
            self._resize(2 * self.capacity)

        self.A_array[self.num_elements] = element
        self.num_elements += 1

    def _resize(self, new_cap: int) -> None:
        
        B_array = self.make_array(new_cap)
        
        for i in range(self.num_elements):
            B_array[i] = self.A_array[i]

        self.A_array = B_array
        self.capacity = new_cap

    def make_array(self, new_cap: int):
        
        return (new_cap * ctypes.py_object)()

arr = DynamicArray4()
print("DynamicArray 4")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A_array)}")

class DynamicArray5(object):
    
    def __init__(self):
        
        self.num_elements = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self) -> int:
        
        return self.num_elements

    def __getitem__(self, k: int) -> Any:
        
        return self.A_array[k]

    def append(self, element: Any) -> None:
        
        if self.num_elements == self.capacity:
            self._resize(2 * self.capacity)

        self.A_array[self.num_elements] = element
        self.num_elements += 1

    def _resize(self, new_cap: int) -> None:
        
        B_array = self.make_array(new_cap)

        for i in range(self.num_elements):
            B_array[i] = self.A_array[i]

        self.A_array = B_array
        self.capacity = new_cap

    def make_array(self, new_cap: int):

        return (new_cap * ctypes.py_object)()

arr = DynamicArray5()
print("DynamicArray 5")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A_array)}")

class DynamicArray6(object):

    def __init__(self):
        
        self.num_elements = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self) -> int:

        return self.num_elements
    
    def __getitem__(self, k: int) -> Any:

        return self.A_array[k]
    
    def append(self, item: Any) -> None:

        if self.num_elements == self.capacity:
            self._resize(2 * self.capacity)

        self.A_array[self.num_elements] = item
        self.num_elements += 1

    def _resize(self, new_cap: int) -> None:
        
        B_array = self.make_array(new_cap)

        for i in range(self.num_elements):

            B_array[i] = self.A_array[i]

        self.A_array = B_array
        self.capacity = new_cap

    def make_array(self, new_cap: int):
        
        return (new_cap * ctypes.py_object)()

arr = DynamicArray6()
print("DynamicArray 6")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A_array)}")

class DynamicArray7(object):

    def __init__(self) -> None:

        self.num_elements = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self) -> int:

        return self.num_elements
    
    def __getitem__(self, k: int) -> Any:

        return self.A_array[k]
    
    def append(self, item: Any) -> None:

        if self.num_elements == self.capacity:
            self._resize(2 * self.capacity)

        self.A_array[self.num_elements] = item
        self.num_elements += 1

    def _resize(self, new_cap: int) -> None:

        B_array = self.make_array(new_cap)

        for i in range(self.num_elements):
            B_array[i] = self.A_array[i]

        self.A_array = B_array
        self.capacity = new_cap

    def make_array(self, new_cap: int):

        return (new_cap * ctypes.py_object)()

arr = DynamicArray7()
print("DynamicArray 7")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A_array)}")

class DynamicArray8(object):

    def __init__(self) -> None:
        
        self.num_elements = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self) -> int:

        return self.num_elements
    
    def __getitem__(self, k: int) -> Any:

        return self.A_array[k]
    
    def append(self, element: Any) -> None:

        if(self.num_elements == self.capacity):
            self._resize(2 * self.capacity)
        
        self.A_array[self.num_elements] = element
        self.num_elements += 1

    def _resize(self, new_cap: int) -> None:

        B_array = self.make_array(new_cap)

        for i in range(self.num_elements):
            B_array[i] = self.A_array[i]

        self.A_array = B_array
        self.capacity = new_cap

    def make_array(self, new_cap: int):

        return (new_cap * ctypes.py_object)()

arr = DynamicArray8()
print("DynamicArray 8")

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}; Size in bytes: {ctypes.sizeof(arr.A_array)}")