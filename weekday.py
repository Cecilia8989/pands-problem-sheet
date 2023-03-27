# this programs outputw whethewer ot not today is a weekkaday.
# weekday.py
'''if today is a weekday it print: Yes, unfortunately today is a weekday
otherwise, it print: It is the weekend, yay!'''
# Author: Cecilia Pastore 

# import datatime module 
import datetime

# return what number of the week today considerin 0 as monday and 6 as sunday using the data funciotn
weekno = datetime.datetime.today().weekday()

# if stantement to print the correct ouput based on the nuber day of the week
if weekno < 5:
    print ("Yes, unfortunately today is a weekday.")
else:  # 5 Sat, 6 Sun
    print ("It is the weekend, yay!")