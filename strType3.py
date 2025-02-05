"""
str (string) is a kind of sequence
str is an immutable iterable type

It means you can use:
    len(), for, [index], [ix1:ix2], in, not in, +, *, ...

"""
# Creation of str that do contain special characters \n, \t, ...

text="line 1\nline 2\nline 3"
print(text)

text="line 1\n\tline 2\nline 3"
print(text)

path="c:\temp\new\file.txt" # \t \n \f
print(path)

path="c:\\temp\\new\\file.txt" 
print(path)

path=r"c:\temp\new\file.txt" # a "raw" str is created
print(path)

url="https://nww.google.ch/ttt" # No special character here 

print(url)