import matplotlib.pyplot as plt
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
squared = np.square(arr)
print(squared)
mean = np.mean(arr)
print("Mean:", mean)

#Generate x values from 0 to 10
x = np.linspace(0, 10, 100)
y = np.sin(x)
# Plot the sine wave
plt.plot(x, y, label='Sine Wave', color='blue')
plt.title('Sine Wave')
plt.show()

