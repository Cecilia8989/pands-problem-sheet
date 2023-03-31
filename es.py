# es.py
''' This programm let the user promp the name of the file in the command line, if the file exist it count how many "e" there are in the file 
if the file don't exist, it inform to the user that the file doesn't exist'''
# Author: Cecilia Pastore 


# import module needed for the script
import sys 
import os  

# get filename from command line argument and letter to count
filename = sys.argv[1] 
letter = "e"


# function to count the number of occurrences of letter in the file
def count_letter(filename, letter):
    with open(filename, "r") as f:
        counter = f.read()
        count = counter.count(letter)
    return (count)

# main programs
# check if file exists, if not prompt inform the user, otherwise count the letter occurrence
if not os.path.exists(filename):
    print(filename, "does not exist, create it or check your spelling ")
else:
    print(count_letter(filename, letter))

