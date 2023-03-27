#collatz.py
''' 
This program takes a positive integer from the user and applies an algorithm to it. 
The algorithm involves dividing the number by 2 if it's even, or multiplying it by 3 and adding 1 if it's odd. 
The intermediate results are stored in a list, and the algorithm is repeated until the result becomes 1. 
If the user enters a negative number, the program asks for a positive number until it is entered.'''
#Author:Cecilia Pastore 

# Create an empty list
numbers = []
# ask to the user to input a positive number 
number = int(input("Please Enter a positive number: "))

# Use a while loop to ensure that the user enters a positive number
while number <=0:
    print("You didn't enter a positive number!")
    number = int(input("Please Enter a positive number: "))
    
# Generate the sequence of numbers until the number 1 is reached.
while number != 1:
 # If the number is even, divide it by 2.
    if (number%2) == 0:
        number = int((number / 2))
    # If the number is odd, multiply it by 3 and add 1.
    else:
        number = int((number * 3 + 1))
     # Append the new number to the "numbers" list
    numbers.append(number)
# Print the numbers in the "numbers" list.
for n in numbers:
    print(n, end= " ")