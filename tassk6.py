ch = input("please enter your character :")
if (ch.isupper()):
    print("the given character" , ch,"is an upper letter")
elif(ch.islower()):
    print("the given character",ch,"is a lower letter")
else:
    print("the given character ",ch,"is not lower or upper")        



"""
Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. 
"""
Keys = ['Sim' ,'Ray', 'Mariam']
Values = ['Maths','Science''English']
dictionary = dict(zip(Keys , Values))
print(dictionary)
    


#Write a program in Python using generators to reverse the string.
def rev_str(my_str):

    value = len(my_str)
    for i in range(value -1, -1, -1):


      yield my_str[i]

for char in rev_str("“Consultadd Training”"):
    print(char)


#5Example of decorators

def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!" 
    return result

print(temperature(20))
   



