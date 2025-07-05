'''
Abstraction is a fundamental concept in programming that allows us to hide complex implementation details and expose only the necessary parts of an object or function.
This makes it easier to work with complex systems by providing a simplified interface.

To use abstraction in Python, we can use abstract base classes (ABCs) 

'''

from abc import ABC, abstractmethod

class A(ABC):
    
    @abstractmethod
    def show(self):
        pass

    def display(self):
        print("This is a display method in class A")

class B(A):
    def show(self):
        print("This is the implementation of the abstract method in class B")

a = B()
a.show()  # Calls the implemented method in class B
a.display()  # Calls the non-abstract method from class A

