# bank.py
# This program ask 2 money quantities on cent to the user and calculate the euro amount 
# Author: Cecilia Pastore 

# Ask to the users 2 quantites in cents
Amount1 = int(input("Please enter an amount (in cents): "))
Amount2 = int(input("Please enter an amount (in cents): "))

# Calculate the amount in Euro/100

AmountInEuro = (Amount1 + Amount2)/100

# stamp the quanity in Euro 

print (f'The sum of there is \u20ac{AmountInEuro}')
