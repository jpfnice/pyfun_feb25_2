"""
str (string) is a kind of sequence
str is an immutable iterable type

It means you can use:
    len(), for, [index], [ix1:ix2], in, not in, +, *, ...

"""
# Methods available:

text="value1:value2:value3:value4"
result=text.split(":")
print(result)

text="value1   value2 value3      value4"
result=text.split()
print(result)

data=['12', '234', '789', '89']
result=";".join(data)
print(result)

name="mArCO"
m1=name.capitalize()
print(m1)
m1=name.upper()
print(m1)
m1=name.lower()
print(m1)
print(name)

file="data_name$$_1234_$$_567.txt"

if "$$" in file:
    file2=file.replace("$$", "")
    print(file2)
    
    


