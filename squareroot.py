#squareroot.py
'''This script ask to the user a positive float number and calculate 
the square root following the newton metod'''
# Author: Cecilia Pastore 

# promp the user to enter a positive floiting number 
user_input=float(input("Please enter a positive float number: "))

# function to handle the case when the input number is not positive    
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
 
# funciont to calculated  the square root based on newton method
def sqrt(user_input):
    approx = 0.5 * user_input
    better = 0.5 * (approx + user_input/approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + user_input/approx)
    return approx

# main programs 
# If user input is negative, call choice_user() to prompt for a positive number
while user_input < 0:
    user_input = choice_user()
    
# Print the square root. Number round to .
square_root = round(sqrt(user_input),1)
print(f'The square rot of {user_input} is approx. {square_root}')


    
    
