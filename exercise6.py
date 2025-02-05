
"""
Exercise 6:
    
Implement a funcion "isprime" to test if a number received as argument is 
a prime number or not.

The value to be tested is N

1)  Is it an int (using isintance())?
2)  Is a positive int and not zero ?
3)  Is it possible to divide it by 2,3,4,5,6, ... N-1 ?
    You can use the modulo operator (%) to check if N can be divided by 2, 
    by 3, by 4, etc ...
    
"""

def isprime(number):
    """
    isprime determine if the argument it receives is a prime number or not
    parameter:
        number: the number to be tested (an int > 0)
    return:
        a bool (True if number is a prime number, False if not)
    """
    if not isinstance(number, int):
        return False
    if number <= 0:
        return False
    for divisor in range(2,number):
        if number % divisor == 0:
            return False
    return True
    
values=[12,13,14,15,-5,23,24,27]
for e in values:
    print(e,"->", isprime(e))