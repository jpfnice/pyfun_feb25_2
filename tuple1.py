
"""
tuple:
    a tuple is an immutable sequence
    len(), for, in, not in, +, [], [:]
"""

data=(23,45,67,12)
print(data, type(data))

data=23,45,67,12
print(data, type(data))

data=tuple([4,5,6,7])
print(data, type(data))

for e in data:
    print(e)
    
