# this programs outputw whethewer ot not today is a weekkaday.
# weekday.py
'''if today is a weekday it print: Yes, unfortunately today is a weekday
otherwise, it print: It is the weekend, yay!'''
# Author: Cecilia Pastore 

# import datatime module and termcolor 
import datetime
from termcolor import cprint

# return what number of the week today considerin 0 as monday and 6 as sunday using the data funciotn
weekno = datetime.datetime.today().weekday()

# if stantement to print the correct ouput based on the nuber day of the week
if weekno < 5:
    cprint ("Yes, unfortunately today is a weekday.",'red')
else:  
    cprint ("It is the weekend, yay!",'red')