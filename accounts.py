#account.py
# This program ask to the user a 10 account number 
# and outputs the account cumber with only the last 4 digits showing
# and the first digits replaced with Xs.
# The program is dinamic and is able to consider account number of any lenght. 
# It read the number of digits enter by the user and it outcome all the number replaced by X apart the last 4.


# ask to the user to input a number of ten digit
Accoun_number_input = input("Please enter an 10 digit account number: ")
# calculate the lenght of the imput
Account_lenght = len(Accoun_number_input)
# get the last 4 charachters of the account number 
Account_last_4_digits = Accoun_number_input[-4:]
print(Account_last_4_digits)
# get how many X the program will need to stamp 
number_of_X = Account_lenght - 4
# print all numbers in the account number as a X apart the last 4 digits
print("X"*(number_of_X)+Account_last_4_digits)