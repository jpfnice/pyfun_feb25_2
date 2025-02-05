"""
str (string) is a kind of sequence
str is an immutable iterable type

It means you can use:
    len(), for, [index], [ix1:ix2], in, not in, +, *, ...

"""
# Creation of str with the help of formated strings

import math
nb=5
text=f"Nb is {nb}"
print(text)
text=f"Nb is {nb} Nb**3 is {nb**3}"
print(text)

text=f"SQRT of Nb is {math.sqrt(nb)} "
print(text)

text=f"SQRT of Nb is {math.sqrt(nb):.2f} "
print(text)

for i in range(1,20):
    print(f"{i:<3} -> {math.sqrt(i):.3f}")

