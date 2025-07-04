input = input("Enter a string: ")
for i in input.split():
    if i[0].isupper():
        print(i[0] , end=" ")