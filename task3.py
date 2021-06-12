#1. Create a list of 10 elements of four different data types like int, string, complex and float.
list = [1,'a',3.6 ,3j,]
print()
#Create a list of size 5 and execute the slicing structure 
list = [1, 6, 8 ,3 ,8,9 ]
print(list[::-1])
print(list[:2])
print(list[4:])

#Write a program to get the sum and multiply of all the items in a given list.
list = [1,6,8,5,9]
list1 = 0
list2 = 1
for i in list:
    list1 += i
for i in list:
    list2 *= i
print("sum of all numbers:", list1)
print("multiply all numbers:", list2)    

# Find the largest and smallest number from a given list.
num = [18, 22, 3, 40, 5, 30, 7, 8, 79]
print("Largest element:", max(num))
print("Smallest element:", min(num))

#Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

num = [22,88,56,87,97,12,14,18]
num = [x for x in num if x%2!= 0]
print(num)

#Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

list = [i * i for i in range(1, 31)]
print("first 5 elements:", list[:4])
print("last 5 elements:", list[::-5])

#Write a program to replace the last element in a list with another list.

lst1 = [1, 3, 5, 7, 9, 10]
lst2 =  [2, 4, 6, 8]
lst1[-1:] = lst2
print(lst1)

#Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
c={}
for i in (a,b): c. update(i)
print(c)
#Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)


#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. 
num = int("input some numbers:")
list = num.split(",")
tuple = tuple(list)
print('list:', list)
print('Tuple:', tuple)