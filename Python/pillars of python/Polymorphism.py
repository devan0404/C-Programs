'''The process by which the same method or function can behave differently based on the object it is called on is known as polymorphism.
1. Overloading: This is the ability to define multiple methods with the same name but different parameters.
    Static polymorphism
    Compile-time polymorphism
    same class

2. Overriding: This is the ability to redefine a method in a subclass that is already defined in its superclass.
    Dynamic polymorphism
    Run-time polymorphism
    different class
'''
class Human:
    def greet_hello(self,name = None):
        if name is not None:
            print("Hi",name)
        else:
            print("Hello")

h = Human()
h.greet_hello()  
h.greet_hello("Alice")
