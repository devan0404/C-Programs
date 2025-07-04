print("Enter the number of elements:")

n = int(input())
a = []

for i in range(n):
    print('Enter element {0}'.format(i + 1))
    a.append(int(input()))

print("The elements in the list are:",a)
print("Enter the element to be searched:\n")

key = int(input())
result = a.count(key)

if result > 0:
    print("The element {0} is present in the list {1} times".format(key, result))
else:
    print("The element {0} is not present in the list".format(key))