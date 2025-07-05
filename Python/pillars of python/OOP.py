'''
The 4 pillers of object-oriented programming (OOP) are:
1. Encapsulation : The process of wrapping data inside a block so that the data is not directly accessible from outside the block. 
        This helps in protecting the block.
2. Inheritance : 
3. Polymorphism
4. Abstraction

'''

class car:
    def __init__(self, speed, color):
        self.__speed = speed # private attribute
        self.__color = color # private attribute

    def set_speed(self, speed):
        self.__speed = speed # setter method to set private attribute
    
    def set_color(self, color):
        self.__color = color # setter method to set private attribute
            
    def get_speed(self):
        return self.__speed # getter method to get private attribute

    def get_color(self):
        return self.__color # getter method to get private attribute

ferrari = car(200, "red")
print(ferrari.get_speed()) # getting speed
ferrari.set_speed(220) # setting new speed