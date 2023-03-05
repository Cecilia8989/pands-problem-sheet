# This script ask to the user a positive float number and calculate the square root following the newton metod
# The script first check that the user inpunt a positive number
# If the number entered by the user is not positvie ask to the user if he wants keep the same number
# but positive or enter a new number 
# based on the answer it take the positive number of the verison or prompt the user to enter a new number 
# at this stage it calculate the square root of the user input number 
# Author: Cecilia Pastore 

# input the user to enter a positive flaot number 
user_input=float(input("Please enter a positive float number "))

# function in case the number is not positive   
def choice_user():
        print("You didn't enter a postive numer")
        print("\t Select what do you want to do: ")
        print("\t\t(a) keep the same number but make it positive")
        print("\t\t(b) enter a new number")
        choice = input("Enter your choice : ")
        # if user choice is "a" transform the number in positve, else prompt the user to enter a new number  
        if choice == "a":
            new_number = abs(user_input)
            print (f"The new number is {new_number}")
            return new_number
        else:
            return float(input("Please enter a positive float number "))
 
# square calculated based on newton method
def sqrt(user_input):
    approx = 0.5 * user_input
    better = 0.5 * (approx + user_input/approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + user_input/approx)
    return approx

#main programs 
while user_input <0:
    user_input = choice_user()

print(sqrt(user_input))
    
    
