

def power(aNumber, exp=2):
    """
    Power is a function to .....
    ....
    
    Parameters
    ----------
    aNumber : an int or a float
    exp : an optional an int or float
        The default is 2.

    Returns
    -------
    result : an int or a float

    """
    result=aNumber ** exp 
    return result
    

nb=12

power()
res=power(nb, 3) # positional argument
print(res)

res=power(nb) # positional argument
print(res)

res=power(exp=3, aNumber=8) # named argument
print(res)

