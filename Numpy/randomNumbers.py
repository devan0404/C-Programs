import numpy as np

#genearate random numbers between 0 and 1

random_numbers = np.random.rand(3)
print("Random Numbers:", random_numbers)

#Generate 5 random integers between 1 and 100
random_integers = np.random.randint(1, 100, size=5)
print("Random Integers:", random_integers)