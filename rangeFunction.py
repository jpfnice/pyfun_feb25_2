
for index in range(5):
    print(index)
    
for index in range(10,20):
    print(index)

for index in range(10,20,2):
    print(index)
    
data=[23,24,35,36,67,89]

for index in range(1,4):
    print(index, "->", data[index])
    
for index in range(len(data)):
    print(index, "->", data[index])
    
for element in data:
    print(element)
    
data=list(range(1000,1020))
print(data, type(data))