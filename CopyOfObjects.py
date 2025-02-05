
"""
Copy of objects

How does the assignment operator (=) works ?

"""

# Version 1: We use the assignment operator NO COPY is done !
    
# data=[5,6,7]

# bis=data # an "alias" of data is created: bis

# print(bis, type(bis))
# print("id of bis", id(bis))
# print("id of data", id(data))

# bis.append(10)
# print(bis)
# print(data)

# Version 2: We use the copy() method:
# data=[5,6,7]

# bis=data.copy() # a copy of data is created: bis

# print(bis, type(bis))
# print("id of bis", id(bis))
# print("id of data", id(data))

# bis.append(10)
# print(bis)
# print(data)

# Version 3: We use the copy() function of the copy module:

import copy
data=[5,6,7]

bis=copy.copy(data) # a copy of data is created: bis

print(bis, type(bis))
print("id of bis", id(bis))
print("id of data", id(data))

bis.append(10)
print(bis)
print(data)