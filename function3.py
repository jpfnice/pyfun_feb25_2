
# def square(aNumber):
#     result=aNumber ** 2 # result is a "local" variable
#     return result

def square(aNumber):
    if isinstance(aNumber, (int, float)):
        result=aNumber ** 2 # result is a "local" variable
        return result
    else:
        print("Wrong argument given: a number is needed")
        return None

nb=12

res=square(nb) # positional argument
print(res)

res=square(aNumber=nb) # named argument
print(res)

res=square("abc") # positional argument
print(res)

print("The end")