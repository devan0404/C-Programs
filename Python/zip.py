rollnos = ['008', '009', '010']
names = ['A', 'B', 'C']
marks = [90, 80, 70]

studentDetails = zip(rollnos, names, marks)
print (studentDetails)

for rollno, name, mark in studentDetails:
    print(f'Roll No: {rollno}, Name: {name}, Marks: {mark}')

atuple = ()

btuple = (1, 2, 3)
print(btuple)
print(type(btuple))
btuple.count(1)

a= 1,2,3
print(a) #comma separated values are considered as tuple
print(type(a)) 

