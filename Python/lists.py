'''
Write a python program on "Lists" that demonstrates the following:
1 Variabes in a list
2 max min sum in a list
3 list concatination
4 list multiplication
5 list with inital values
'''

freq = [0] * 10
print (freq)

# LIST Comprehension 
a = [1, 2, 3, 4, 5,6,7,8,9,10]
even_numbers= [i for i in a if i % 2 == 0]
odd_numbers = [i for i in a if i % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

gt_5 = [i for i in a if i >5] 
lt_5 = [i for i in a if i < 5]
print("Numbers greater than 5:", gt_5)
print("Numbers less than 5:", lt_5)

# PROBLEM STATEMENT: Jones is an angry professor known for his strict nature. he is adament about his students reaching class on time.
# He has a rule that if at least 3 students are late, he will cancel the class.
# Write a program to check if the class is cancelled or not based on the students' arrival using list comprehension.
# Asked by accenture , TCS, Wipro

list = [-1,-2,4,2,0]
decision = [i for i in list if i <= 0]
print("Take Class" if len(decision) >= 3 else "No class")