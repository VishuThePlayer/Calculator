# 1st project on github
print("Welcome to my Calculater")                                 #prints the command
#                      ------------------------>                 #defining the function to call it late
def add (x,y):                                                   #made a function whoose name is add
        result = x+y                                             #adding the value i.e. x +y
        print("Yeah ! Your answer is :", result)
        return result
def multiply(x,y):
        result = x*y
        print("Yeah ! Your answer is :", result)
        return result

def substraction(x,y):
        result = x-y
        print("Yeah ! Your answer is :", result)
        return result

def division(x,y):
        result =x/y
        print("Yeah ! Your answer is :", result)
        return result


while True:
        choice = int(input("\nWhat Would YOu Like to Do Kindly select it: \n 1.Addition \n 2.Substrction \n 3.Multiplication \n 4.Division \n Enter--> "))     # basically as the name suggests it will ask your choice i.e. what you want to do

        number1 = int(input("Enter THe Number 1: "))

        number2 = int(input("Enter THe Number 2: "))

        if choice == 1:
                add(number1,number2)


        elif choice == 2:
                substraction(number1, number2)

        elif choice == 3:
                multiply(number1, number2)

        elif choice == 4:
                division(number1, number2)

        else:
                print("Wrong Input Try AGain!")



