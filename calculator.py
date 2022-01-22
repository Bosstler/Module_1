#Using functions and classes, create a calculator that allows an user to 
# manipulate any number they choose with correct mathematical function

# #Introduce user to the program and get a number from them
# print('Welcome to the calculator program!')
# number = float(input('What number would you like to start with? '))

""" Calculator
----------------------------------------
"""
print(" Python Calculator Program!")
#create a function for addition
def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

#create a function for subtraction
def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    t = 0
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

#create a function for multiplication
def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

#return an average for given values
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

#create a function that allows the user to use the same total for different functions i.e, multiplication, then division, etc
# def continue_():
#     while cont.lower() == 'y':
#         running_total = list[0]

#Excecute the calculator program
# // main...
while True:
    list = []
    # print(" Python Calculator Program!")
    #Create a "graphic" the user can see and select choices from
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' to quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
            # cont = str(input('Would you like to continue with this same value? (y/n) '))
            # if cont.lower() == 'y':
            #     continue_
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("-------Sorry, invilid character--------")
    else:
        break
