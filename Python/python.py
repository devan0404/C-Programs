# DTL -->  Dynamically Typed Language 
# Python is a dynamically typed language, meaning that variable types are determined at runtime.
a = 10
b= 2.5
c = "Hello, World!"
d = True
print(type(a), type(b), type(c), type(d))

for i in range(1, 11):
    print(i, end=" \t")

#Printing multiplication tables

n1 = int(input("Enter the number for multiplication table: "))
n2 = int(input("Enter the number for multiplication table: "))
for i in range(n1,n2+1):
    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print() 
        