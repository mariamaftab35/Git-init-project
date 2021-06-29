#Write a program in Python to allow the error of syntax to be handled using exception handling.
a = 12
x = "welcome"
try:
    print("inside try")
    print(a + x)
    print("using orginal data types")
except TypeError:
    print(str(a) + x)


"""
2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again.
"""
import sys
with open(sys.argv[1] , 'r') as my_file:
    print(my_file.read())



"""
3. Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits”
"""
def signal_num(prompt):
    num = ""
    while True:
        num = raw_input(prompt)
        if len(num) == 4:
            try:
                return int(num)
                except ValueError:
                    print ("Error , you must enter the number")
        else:
            print("Try again")        


#4Create a login page backend to ask users to enter the username and password.
counts = 0
while counts<3:
    username = input("username?")
    password = input("password?")
    if username =="dell" and password =="black":
        print("welcome")
    else:
        counts+=1
        print("incorrect")
        if counts==3:
            print("Too many attempts")

        

"""
5:Read doc.txt file using Python File handling concept and return only the even length string from
the file.
"""                    
L = ["Where do you need to return the data string \n", "Which is of even length \n", "Make sure your return \n"]

with open("myfile.txt" ,"W") as file1:
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()
with open("myfile1.txt", "r+") as file1:
    print(file1.read)    

