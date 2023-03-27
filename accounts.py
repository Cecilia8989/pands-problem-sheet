# account.py
'''
This program masks a user's inputted account number by replacing all but the last 4 digits with X's. 
It can handle account numbers of any length.
'''
# Author:Cecilia Pastore 

# asks to the user to input an account number
account_number_input = input("Please enter an account number: ")
# calculate the lenght of the input
account_lenght = len(account_number_input)
# get the last 4 charachters of the account number 
account_last_4_digits = account_number_input[-4:]
# calculate the number of X's needed to replace the remaining digits
number_of_X = account_lenght - 4
# print the account number with all but the last 4 digits replaced with X's
print("X"*(number_of_X)+account_last_4_digits)