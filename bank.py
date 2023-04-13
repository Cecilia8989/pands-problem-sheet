# bank.py
# This program ask 2 money quantities on cent to the user and calculate the euro amount 
# Author: Cecilia Pastore 

# Ask the user for two quantities in cents
cents1 = int(input("Please enter an amount (in cents): "))
cents2 = int(input("Please enter an amount (in cents): "))

# Calculate the total amount in euro, by using and integer division 
sum_cents = cents1 + cents2
total_euro = sum_cents // 100 
total_cents = sum_cents % 100 


# Print the total amount in euro, with a Euro sign symbol
print (f'The sum of these is \u20ac{total_euro}.{total_cents}')
