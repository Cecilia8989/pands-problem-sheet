#collatz.py
# This program:
# - ask to the user to enter a positive number
# - if the user enter a negative number he ask him to enter again a positive number
# - take the positive number and devide it for 2 if it is a even number 
#   or moltiply per 3 + 1 if it is an odd number
# - print the new number
# - repet the while loop until the number is one
# - print end at the end  

# ask to the user to input a positive number 
number = int(input("Please Enter a positive number: "))

# First while loop to have the user enter a positive number before to start
# the second while loop
while number <=0:
    print("You didn't enter a positive number!")
    number = int(input("Please Enter a positive number: "))
    
# second while loop to be excecuted until the result number is 1    
while number != 1:
# if the number is an even number devide it for 2 and print the new number
    if (number%2) == 0:
        number = int(number / 2)
        print(number)
# if the number is an odd number moltiply it for 3 and add 1
# print the new number 
    else:
        number = int(number * 3 + 1)
        print(number)
# when the number become 1 end the while loop and print "End"
print("End")
    
