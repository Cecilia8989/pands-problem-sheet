
#es.py
#This programm let the user promp the name of the file in the command line, if the file exist it count how many "e" there are in the file 
#if the file don't exist, it inform to the user that the file doesn't exist
#Author: Cecilia Pastore'''


# import module needed for the script
import sys 
import os  

# function to count the number of occurrences of letter e (lower) in the file 
def count_letter_e(filename, letter):
    with open(filename, "r") as f:
        counter = f.read()
        count = counter.count(letter)
    return (count)

# function to count the number of occurrences of letter E (upper) in the file 
def count_letter_E(filename, letter):
    letter_upper = letter.upper()
    with open(filename, "r") as f:
        counter = f.read()
        count = counter.count(letter_upper)
    return (count)

# function to count the number of occurrences of letter e and E in the file 
def count_letter_e_and_E(filename, letter):
    with open(filename, "r") as f:
        counter = f.read().lower()
        count = counter.count(letter)
    return (count)

# function to promp the user to enter a choice 
def user_choice_input():
    print (" What do you want to count: ")
    print("\t 1. e (lower case)")
    print("\t 2. E (upper case)")
    print("\t 3. e and E")
    user_choice = int(input("Please make your choice: ")) 
    return user_choice

# main program 

# get filename from command line argument and handle the case user didn't put any 
try:
    filename = sys.argv[1]
except IndexError:
    sys.exit ("You didn't enter any file name. Please execute the script again")

# check if file exists. if the file doesn't exist exit the programm else prompt the user for a choice 
if not os.path.exists(filename):
    sys.exit(filename + "does not exist, create it or check your spelling ")
else:
    user_choice = user_choice_input()

letter = "e" 

# while loop to promt the user to enter a valid choice 
options = [1,2,3]
while user_choice not in options:
    print( "Please enter a choice between 1, 2 or 3")
    user_choice = int(input("Please make your choice: ")) 
    
# if statements to execute a count based on user choice 
if user_choice == 1:
    count =  count_letter_e(filename, letter)
    letter = "e"
elif user_choice == 2:
    count = count_letter_E(filename, letter)
    letter = "E"
else:
    count =count_letter_e_and_E(filename, letter)
    letter = "e and E"

# Print the final count 
print (f'In the file there are {count} letters {letter}' )


