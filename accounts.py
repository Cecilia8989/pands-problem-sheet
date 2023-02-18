# account.py
# Author:Cecilia Pastore 
# This program ask to the user a 10 account number 
# and outputs the account number with only the last 4 digits showing
# and the previous ones replaced with Xs
# The program is dinamic and is able to consider account number of any lenght. 
# It will read the number of digits enter by the user and it will outcome all the numbers replaced by X apart the last 4.


# ask to the user to input a number of ten digit
Accoun_number_input = input("Please enter an account number: ")
# calculate the lenght of the imput
Account_lenght = len(Accoun_number_input)
# get the last 4 charachters of the account number 
Account_last_4_digits = Accoun_number_input[-4:]
# get how many X the program will need to stamp 
number_of_X = Account_lenght - 4
# print all numbers in the account number as a X apart the last 4 digits
print("X"*(number_of_X)+Account_last_4_digits)