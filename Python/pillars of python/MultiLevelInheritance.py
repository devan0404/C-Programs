'''
Multi Level Inheritance 
simple calculator : addition
advanced calculator : subtraction
super advanced calculator : multiplication and division
'''

class SimpleCalculator:
    def add(self, a, b):
        return a + b

class AdvancedCalculator(SimpleCalculator):
    def subtract(self, a, b):
        return a - b 
    
class SuperAdvancedCalculator(AdvancedCalculator):
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

calc1 = SimpleCalculator()

print('------------------------')
print(calc1.add(10, 5))
calc2 = AdvancedCalculator()
print('------------------------')
print(calc2.subtract(10, 5))
calc3 = SuperAdvancedCalculator()
print('------------------------')
print(calc3.multiply(10, 5))
print('------------------------')
print(calc3.divide(10, 5))
print('------------------------')
