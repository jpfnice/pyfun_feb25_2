
myfile=open("data.txt")

total=0
for line in myfile:
    print(line) # "12,23,56"
    result=line.split(",") # result is a list of str
    print(result)
    for e in result: # result is something like ['12', '23', '56\n']
        total += int(e)
        
print("Total is", total)       
myfile.close()

