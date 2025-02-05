# Here I DEFINE the function removeALL:
def removeAll(alist, element):
    while element in alist:
        alist.remove(element)
        
data=[5,6,7,5,5,7,8,5]
print(data)

removeAll(data, 5) # Here I CALL the function removeALL
print(data)

