#Write a program to reverse a string.
str = "Hello World" [::-1]
print(str)

#Write a function that accepts a string and prints the number of uppercase letters and lowercase
def string(s):
    d = {"Upper_Case":0, "Lower_Case":0}
    for i in s:
        if i.isupper():
            d["Upper_Case"] += 1
        elif i.lower():
            d["Lower_Case"] += 1
        else:
            pass
    print("original string" , s)
    print("No of upper case letters" , d["Upper_Case"])
    print(("No of lower case letters" , d["Lower_Case"]))      
string("A black Cat and White Dog")     

#Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,5,9,5,3,7,3,2]))     

"""
4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.
"""

items = [n for n in input().split('-')]
items.sort()
print('-'.join(items))
print("sorted")

"""
Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
"""
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;
for l in lines:
    print(l)
"""
6. Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console.    
"""

def calculateSum(a,b):
    s = int(a) + int(b)
    return s

a = "10"
b = "30"
sum = calculateSum (a,b)
print("Sum", sum)

"""Define a function that can accept two strings as input and print the string with the maximum length
in the console.
"""
def printValue (s1,s2):
    len1 = len(s1)
    len2 =len(s2)
    if len1 > len2:
        print(s1)
    elif len2 > len1:
        print(s2)
    else:
        print(s1)
        print(s2)

printValue("two","four")            

"""
8. Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).
"""


def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)

printTuple()

"""
9. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
"""
def showNumber(limit):
    for i in range(0,limit):
        if i ==0:
            print(i,end=" ")
            print("Even")
        elif i%2==0:
            print(i,end="")
            print("Even") 
        else:
            print(i,end="")
            print("Odd")

print(showNumber(7))

"""10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)
"""
def even (x):
    return x%2==0
evenNumber = filter(even,range(1,21))    
print(list(evenNumber))

