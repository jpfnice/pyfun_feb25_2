
phone={"mario":45676, "julia":89876, "yohan":76554}
print(len(phone))

print("Phone number of yohan", phone["yohan"])
print("Phone number of julia", phone["julia"])
phone["yohan"]=67665
print("Phone number of yohan", phone["yohan"])

if "jean" in phone:
    print("Phone number of yohan", phone["jean"])
print(phone) 
   
phone["louis"]=98889

print(phone)
del phone["julia"]
phone["julie"]=98889

print(phone)

for k in phone.keys():
    print(k)

for k in phone.values():
    print(k)
    
for k,v in phone.items():
    print(k, v)
    
