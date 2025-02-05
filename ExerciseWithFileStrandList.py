
"""
Given a file with this format (you can use "data.txt" for instance or create your own test file):

    x1:0.34;x2:0.56
    x1:0.24;x2:0.45
    x1:0.27;x2:0.55
    ...

extract out of it the numerical values associated with x1 and x2.
The values associated with x1 will be stored in a list with the name X1.
The values associated with x2 will be stored in a list with the name X2.

To extract the 2 float out of each line you could:
    1) use slices
    2) use 2 split() methods
    3) use another strategy ??
    
Create a list Y1 that will contain the cosine of each value stored in X1 
(use the math.cos() function)

Create a list Y2 that will contain the sine of each value stored in X2 
(use the math.sin() function)

Once the 4 lists will be created I will show you how to plot the corresponding points (X1,Y1, X2,Y2).
"""

import math

X1=[]
X2=[]
Y1=[] # Will be the cosine of X1
Y2=[] # Will be the sine of X2

dataFile=open("data.txt") # a file Object is iterable

for line in dataFile:
    # line= "   x1:0.34;x2:0.56\n" 
    line=line.replace(":", ";")
    # line= "   x1;0.34;x2;0.56\n" 
    result=line.split(";")
    # result = ['  x1', '0.34', 'x2', '0.56\n']
    
    if len(result) == 4:
        v1=float(result[1])
        #secondValue=result[3].strip("\n") # '0.56\n'
        v2=float(result[3]) # '0.56'
        X1.append(v1) 
        X2.append(v2) 
    else:
        print("The line:", line, "does not have the expected format!")

dataFile.close()


for e in X1:
    Y1.append(math.cos(e))
    
for e in X2:
    Y2.append(math.sin(e))
    
print("X1:", X1)
print("X2:", X2)

print("Y1:", Y1)

# To have a better control on the way the elements of Y1 are formatted:
    
print("Y1", end=':')
for e in Y1[0:-1]:
    print(f" {e:.2f}", end=",")
print(f"{Y1[-1]:.2f}")    

print("Y2:", Y2)

#To plot the corresponding points:
    
import matplotlib.pyplot as plt

# 1 figure  is composed of 1 to n axes
# You a plot a shart in one axes or another

fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,4)
ax1.plot(X1,Y1)
ax2.plot(X2,Y2)
plt.show()

# plt.plot(X1,Y1,".",  label="Cosine")
# plt.plot(X2,Y2, ".", label="Sine")
# plt.legend()
# plt.show()



