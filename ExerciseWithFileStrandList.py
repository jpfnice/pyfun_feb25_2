
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

X1=[]
X2=[]

myfile=open("data.txt")

for line in myfile:
    print(line) 
    
myfile.close()
