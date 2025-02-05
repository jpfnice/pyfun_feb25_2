
"""
Write a Python script that prompts the user for several numbers (when the user enter the string "stop", the script stop asking for numbers).

The numbers entered are stored into a list one after the other.

(Within a loop you prompt the users for numbers using the input() function. Each time a new value is given yoiu append it to a list initialy empty)

After having retrieved all the numbers, print the list.

The script will then compute and print the minimum, the maximum and the mean of the different numbers present in the list.

You can also compute the "truncated mean" of the elements present into the list, i.e. the mean of all elements except the smallest and largest elements:
    If the original list is:
        [1,2,3,1,2,5,1,5,6,2,6]
    The truncated mean will take into account only these elements:
        [2,3,2,5,1,5,2]
        
"""
import statistics
numbers=[]   # Creation of an empty list <=> numbers=list()

# Step 1:
while True:
    answer=input("Enter an int or 'stop': ")
    if answer=='stop':
        break
    else:
        answer=int(answer)
        numbers.append(answer)

print(numbers) 

# How to determine the largest element (the largest int) of the list numbers ?
# 1) may be there is a predefine function or method that offer this facility ?
#    If you are looking for the methods available for list you can use this
#    Python statement:  help(list)
#    If you are looking for a builtin function, you can have a look at the 
#    official Python doc: https://docs.python.org/3.12/library/functions.html
#    If you have an idea of the name of the function you are looking for you
#    can use the search engine provided here: https://docs.python.org/3.12/library/
#    You can also use google, bing, etc ...
# 2) you can determine the maximum by comparing the different elements 
#    of numbers one with the other
# 3) you can sort the list and then get the minimum (first element) and the 
#    maximum (last element) 

# How to determine the mean of the elements present into numbers ?
# 1) may be there is a predefine function or method that offer this facility ?
# 2) you can, with the help of a loop (while or for), iterate trough the list
#    and add its element one by one. At the end of the loop, you divide the sum
#    obtained by the number of element present into the list (computed with the help 
#    of len())
# 3) may be there is a predefine function or method that offer the possibility to 
#    sum the elements ? It will then be easy to compute their mean.

print("Maximum", max(numbers))
print("Minimum", min(numbers))
print("Mean", sum(numbers)/len(numbers))
print("Mean", statistics.mean(numbers))

# Another strategy to get the min and max 
numbers.sort()
print("Maximum", numbers[-1])
print("Minimum", numbers[0])

# If I want to compute the minimum, the maximum and the sum with my own code:
currentmin=numbers[0]
currentmax=numbers[0]
currentsum=numbers[0]

for index in range(1, len(numbers)):
    if numbers[index] > currentmax:
        currentmax = numbers[index]
    if numbers[index] < currentmin:
        currentmin = numbers[index]  
    currentsum += numbers[index]

print("Maximum", currentmax)
print("Minimum", currentmin)
print("Mean", currentsum/len(numbers))


# data=[1,2,3,1,2,5,1,5,6,2,6]
# How can I compute the truncated mean ?
# 1) using the remove() you remove the min and the max from numbers.
#    How long as the minimum is present (you can use "in" to check that) you
#    call remove(minimum). You do the same with the maximum. The you compute 
#    the mean
# 2) 2.1 sort the list:
#           data will be [1, 1, 1, 2, 2, 2, 3, 5, 5, 6, 6]
#   2.2 with the help of count() I count the number of time the min and the max do
#       appear: the minimum (1) appears 3 times, the maximum 2 times
#   2.3 you can then create a slice like this on: numbers[3:-2]

# Version 1:
# print("Before",numbers)
# minimum=min(numbers)
# maximum=max(numbers)

# while minimum in numbers:
#     numbers.remove(minimum)

# while maximum in numbers:
#     numbers.remove(maximum)
# print("After",numbers)
# print("Truncated mean: ", sum(numbers)/len(numbers))

# Version 2:
numbers.sort()
print(numbers)
maxocc=numbers.count(numbers[-1])
minocc=numbers.count(numbers[0])
print(minocc, maxocc)
print(numbers[minocc:-maxocc])
print("Truncated mean: ", sum(numbers[minocc:-maxocc])/len(numbers))




# index=0
# while index < len(numbers):
#     print(numbers[index], end=":")
#     index+=1
    
# print()  
# print("*"*40)

# for element in numbers:
#     print(element)
    
# print("*"*40)    

# for element in numbers[1:4]:
#     print(element)
    
# print("*"*40)    
