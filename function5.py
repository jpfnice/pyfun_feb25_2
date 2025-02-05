
"""
addition() is a function that accept a variable number of arguments

"""
def addition(*args):
   # print("args is", args)
   # print("Number of arguments received", len(args))
   #print("First argument received", args[0])
   #print("Last argument received", args[-1])
   total=0
   for e in args:
       total += e
   return total
   
result=addition()   # -> 0
print(result)
result=addition(12) # -> 12
print(result)
result=addition(12,67,78,89) 
print(result)
result=addition(12,67,78,89,89,5,221,33)
print(result)


