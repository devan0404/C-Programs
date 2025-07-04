#Arbitrary keyword arguments

def name(**kwargs):
    print ('The name of the student is ',kwargs['s1'])


name(s2='sahana', s1='sanjay', s3='siddharth')

#default parameter value

def fav_subject(fav = 'Python'):
    print('The favourite subject is', fav)

fav_subject('C++')
fav_subject('Java') 
fav_subject()  

#lambda function

simple_interest = lambda p, r, t: (p * r * t) / 100
area_of_circle = lambda r: 3.14 * r * r

interest = simple_interest(1000, 5, 2)
print('Simple Interest:', interest)
area = area_of_circle(5)
print('Area of Circle:', area)