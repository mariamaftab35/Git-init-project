user_input1 = eval(input("""Enter your choice(Option #):
1. Addition
2. Subtraction
3. Division
4. Multiplication
5. Average
"""))
if user_input1 in [1, 2, 3, 4, 5]:
    first = eval(input("Enter first number:"))
    second = eval(input("Enter second number:"))
    if user_input1 == 1:
        print("Addition:", first + second)
    elif user_input1 == 2:
        print("Subtraction:", first - second)
    elif user_input1 == 3:
        print("Division:", first / second)
    elif user_input1 == 2:
        print("Multiplication:", first * second)
    else:
        first1 = eval(input("Enter the third number:"))
        second1 = eval(input("Enter fourth number:"))
        print("Average:", sum([first, second, first1, second1]) / 4)
else:
    print("ZSA")


"""
1. Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “c” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.
"""
num1 = eval(input("enter your value"))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("Consultadd Python Training")
elif num1 % 3 == 0:
    print("Consultadd")
elif num1 % 5 == 0:
    print("“Python Training") 

# Program for the given flowchart
x, y, z = 12, 22, 40
avg = (x + y + z) / 3
print("avg = ", avg)
if avg > x and avg > y and avg > z:
    print("Average is higher than x, y, z")
else:
    if avg > x and avg > y:
        print("Average is higher than x, y, z")
    elif avg > x and avg > z:
        print("Average is higher than x, z")
    elif avg > y and avg > z:
        print("Average is higher than y, z")
    elif avg > x:
        print("Average is higher than x only.")
    elif avg > y:
        print("Average is higher than y only.")
    elif avg > z:
        print("Average is higher than z only.")       

"""
Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”
"""
while True:
    try:
        num = int(input("enter the value:"))
        if num < 0:
            print("its over")
            break
        else:
            print("Good Going")
    except ValueError:
                pass



#5.   Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.            

list = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        list.append(i)
print(list)        

#7 Write a program that prints all the numbers from 0 to 6 except 3 and 6. 

for i in range(6):
    if (i == 3 or i == 6):
        continue
    print(i, end = '')
print('\n')    
#8:Write a program that accepts a string as an input from user and calculate the number of digits and letters.



str = input("enter the string:")
digit = 0
letter = 0
for i in str:
    if i.isnumeric():
        digit+= 1
    elif i.isalpha():
        letter+= 1
    else:
        pass
print("letter", letter)
print("digit", digit)    


#9 guess the luck number
guess = 57
while True:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        user_input, answer = input("Do you want to guess again? (Enter number & Yes to continue. Enter No to stop")
        if user_input != guess and answer.lower() == 'yes':
            continue
        elif user_input == guess:
            break
        elif answer.lower == 'no':
            break


#10  Write a program that asks five times to guess the lucky number. Use a while loop and a counter

import random
guess = 57
counter = 0
while counter < 5:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        print("Good guess!")
        guess = random.randint(1, 100)
    else:
        print("Try again!")
    counter += 1
print("Game over!")

#11. In the previous question, insert break after the “Good guess!” print statement.

import random
guess = 57
counter = 0
while counter < 5:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        print("Good guess!")
        break
    else:
        print("Try again!")
    counter += 1
print("Sorry but that was not very successful!")