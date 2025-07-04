'''
Use the filter() to filter out even numbers from a list of integers.

Use map() to square each number in a list of integers.
'''
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x : x % 2 == 0, numbers)
print(list(even_numbers))

squared_numbers = map(lambda x : x ** 2, numbers)
print(list(squared_numbers))

product = reduce(lambda x,y : x * y, numbers)
print(product)

#importing modules in python
#import module_name
#from module_name import function_name
#from module_name import * 
#from module_name import function_name as alias_name #EXAMPLE: from math import sqrt as square_root