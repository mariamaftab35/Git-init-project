print("Hello World")
print("assigning values of different datatypes")
a, b, c, d = 4, "mariam", 10.8, True
print(a)
print(b)
print(c)
print(d)

# Swap two numbers using a third variable and do the same task without using any third variable.
x = 7
y = 10
print("before swapping ")
print("value of x:" ,x,"and y:",y)
#swapping code
x, y = y, x
print("after swapping")
print("value of x:" ,x, "and y:",y)

#. Swap two numbers using a third variable
num1 = int(input("enter the first value num1: "))
num2 = int(input("enter the second value num2: "))
tempvar = num1
num1 = num2
num2 = tempvar
print("after swap")
print("value of num1 is :", num1)
print("value of num2 is :", num2)


#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x

name = input("enter your name\n")

age = int(input("enter your age\n"))
print(name,age)

#5. Write a program to complete the task given below:
a = 5
b = 7
z = a + b
z +=30
print(z)

#6. Write a program to check the data type of the entered values.

name = input("enter name\n")

num = 100.99
age = int(input("age please\n"))
print("datatype:",type(name),"datatype :", type(num),"datatype:", type(age))


#Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and



var1 = ('helloClass')  #lowerCamel
var2 = ("HelloClass")  #UpperCamel
var3 = ('hello_class')  #snake_case

print("variable:",var1, "variable:", var2,"variable:",var3)

#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’

#Answer Yes, variables in Python can be reassigned to a new value that is a different data type from its 