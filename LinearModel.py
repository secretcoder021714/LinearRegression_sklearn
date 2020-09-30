#This is the import Section
import numpy as np
import matplotlib.pyplot as plt
x = np.array([10,20,30,40,50,60,70,90])
y = x*2+10

plt.plot(x , y)
plt.title("X v/s y")
plt.show()

print("x is : ",x)
print("y is : ",y)

from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(x,y)
