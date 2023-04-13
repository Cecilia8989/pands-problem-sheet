# pands-problem-sheet

## Programming screepting weekly task

### General information

This document contain an explanation of every program created as weekly task during the module programming screepting. In the table of content you will be able to navigate to each single script.

### Technologies
- Python 3.19

### Table of content
* [Task week 01 helloworld.py](https://github.com/Cecilia8989/pands-problem-sheet/blob/main/README.md#task-week-1---helloworldpy)
* [Task week 02 bank.py](https://github.com/Cecilia8989/pands-problem-sheet/blob/main/README.md#task-week--2---bankpy)
* [Task Week 03 accounts.py](https://github.com/Cecilia8989/pands-problem-sheet/blob/main/README.md#task-week-3---accountpy)
* [Task Week 04 collatz.py](https://github.com/Cecilia8989/pands-problem-sheet/blob/main/README.md#task-week-4---collatzpy)
* [Task Week 05 weekday.py](https://github.com/Cecilia8989/pands-problem-sheet/blob/main/README.md#task-week-5---weekdaypy)
* [Task Week 06 squareroot.py](https://github.com/Cecilia8989/pands-problem-sheet/blob/main/README.md#task-week--6---squareroot)
* [Task Week 07 es.py](https://github.com/Cecilia8989/pands-problem-sheet/blob/main/README.md#task-week-7---es)
* [Task Week 08 plottask.py](https://github.com/Cecilia8989/pands-problem-sheet/blob/main/README.md#task-week-8---plottaskpy)

### Task Week 1 - helloWorld.py

#### Description 

<details>
    <summary>Task requested:</summary>
           <p>

>Commit and push a file to the problem sheet called helloworld.py

</p>
</details>

The script print "Hello World!" when executed. 

- - - -

#### How it works

It a command that once executed it print Hello World!.

<details>
           <summary>Code comments</summary>
           <p>
Print Hello world!

```python
print("Hello World!")
```
</p>
</details>

- - - -
<details>
           <summary>Sources</summary>
           <p>

-	Lecture Week 01 
             </p>
</details>

### Task Week  2 - bank.py

**Script modified after lecture feedback**

#### Description 

<details>
    <summary>Task requested:</summary>
           <p>

>When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
>
>Write a program called bank.py 
>
>The program should:
>Prompt the user and read in two money amounts (in cent)
>Add the two amounts
>Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
>

```sh
$ python bank.py
Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45

```
</p>
</details>

This program is designed to ask the user for two monetary quantities in cents and then calculate the total amount in euros. The resulting amount is displayed with the Euro sign symbol.

- - - -

#### How it works

Here the main steps of the program:

- The program can be run by executing the **"bank.py"** script. 
- The program will prompt the user to enter a first quantity in cents.
- A  second quantity in cents will be asked to the user.
- It calculates the total amount in euros by adding cents1 and cents2 together, and then using integer division (//) to obtain the whole number of euros without any decimals.
- It calculates the remaining cents after the addition of cents1 and cents2 using the modulo operator (%), which gives the remainder of the division. 
- The total amount in Euro will be displayed with the Euro Symbol


<details>
           <summary>Code comments</summary>
           <p>

The user is asked for two quantities in cents. The quantities need to be integer (absolute number).
```python
cents1 = int(input("Please enter an amount (in cents): "))
cents2 = int(input("Please enter an amount (in cents): "))
```

It calculates the total amount in euros by adding cents1 and cents2 together, and then using integer division (//) to obtain the whole number of euros without any decimals. The result is stored in the variable total_euro.             
```python
sum_cents = cents1 + cents2
total_euro = sum_cents // 100
```
               
It calculates the remaining cents after the addition of cents1 and cents2 using the modulo operator (%), which gives the remainder of the division. The result is stored in the total_cents
```python
total_cents = sum_cents % 100 

```
Print the total amount in Euro with the [Euro symbol](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python#:~:text=Euro%20is%20encoded%20as%2080h%20%280x80%29%20in%20the,as%20others%20said%2C%20using%20the%20correct%20encoding%20%28utf-8%29%3A).
````python
print (f'The sum of these is \u20ac{total_euro}.{total_cents}')
````



</p>
</details>

- - - -
<details>
           <summary>Sources</summary>
           <p>

- [how to write the euro sign in phyton without the keybord](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python#:~:text=Euro%20is%20encoded%20as%2080h%20%280x80%29%20in%20the,as%20others%20said%2C%20using%20the%20correct%20encoding%20%28utf-8%29%3A)
- Readme file:
  - [How to add a link or Hyperlink in Readme.MD file](https://devcracker.medium.com/how-to-add-a-link-or-hyperlink-in-readme-md-file-68752bb6499e)
  - [Manually create a Markdown table of contents for your GitHub README](https://www.setcorrect.com/portfolio/work11/)
  - [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
  - [How to write a good README for your GitHub project?](https://bulldogjob.com/readme/how-to-write-a-good-readme-for-your-github-project)
  - [How to Write a Good README File for Your GitHub Project](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
  - [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
  - [How To Write A Good README File](https://dev.to/merlos/how-to-write-a-good-readme-bog)
  - [Division Operators in Python](https://www.geeksforgeeks.org/division-operators-in-python/)


</p>
</details>

### Task Week 3 - account.py 

#### Description 

<details>
    <summary>Task requested:</summary>
           <p>

>Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
>
>Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).


```sh
$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
```
> Extra:
>
>Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
</p>
</details>

I decide to develop the program following the "extra" request.

This program is designed to ask the user for an account number and print the account number with all the digits replaced with X's except for the last 4 digits. 
It can handle account numbers of any length, but the number of digits replaced with X's will vary depending on the length of the account number.

- - - -

#### How it works

Here the main steps of the program:
- The program can be run by executing the **"account.py"** script
- The user will be asked to enter an account number 
- The program will then calculate the length of the account number and get the last 4 digits
- It will calculate the number of X's that are needed to replace the remaining digits
- It will then display the masked account with all the digits replaced by X's except the last 4 digits 

<details>
           <summary>Code comments</summary>
           <p>

Get the user to enter an account number of any length
```python
account_number_input = input("Please enter an account number: ")
```
The length of the account number input by the user is calculated
```python
account_lenght = len(account_number_input)
```
Obtain the last 4 digits of the account number
````python
account_last_4_digits = account_number_input[-4:]
````
Calculate the number of X's needed to masks all but the last 4 digits with X's. 
````python
number_of_X = account_lenght - 4
````
Print the masked account.
````python
print("X"*(number_of_X)+account_last_4_digits)                    
````
</p>
</details>

- - - -
<details>
           <summary>Sources</summary>
           <p>

- [Get the last four number of a string in phyton ](https://reactgo.com/python-get-last-four-characters/#:~:text=To%20access%20the%20last%204%20characters%20of%20a,position%20of%20a%20string.%20Here%20is%20an%20example%3A)
- [How do I print a number n times in python?](https://stackoverflow.com/questions/56091904/how-do-i-print-a-number-n-times-in-python)
- [print a variable](https://pytutorial.com/python-variable-in-string/)

</p>
</details>


### Task Week 4 - collatz.py

#### Description 

This script prompt the user to enter a positive number and, depending on whether the number is even or odd, perform a calculation until the number is 1. The program will either divide the number by 2 (if it is even) or multiply it by 3 and add 1 (if it is odd). Each new number will be added to a list, and the full list will be printed out when the loop is exited.

<details>
    <summary>Task requested:</summary>
           <p>

>Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.
Push the program in your pands-problem-sheet GitHub repository (like you do for all the weekly tasks).
Example of it running:
>

```sh
$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1
```
</p>
</details>

- - - -


#### How it works

Here the main steps of the program:
1. The program can be run by executing the **"collantz.py"** script
2. The script first prompts the user to enter a positive number. A first while loop is used to check if the user enters a positive number. If they do, the script exits the first while loop, If the user enters a negative number, the script will continue to prompt the user to enter a positive number until one is provided.
3. The script will check whether the number is even or odd and cased on that perform a calculation.
   - If the number is even, the script divides it by 2 and adds it to the "numbers" list. 
   - If it is odd, the script multiplies the number by 3, adds 1, and then adds it to the "numbers" list. 
4. The while loop will continue until the number is one.
5. When the number is 1 the while loop will exit and the full list will be printed 

<details>
           <summary>Code comments</summary>
           <p>

Create an empty list to store the generated sequence of numbers
```python
numbers = []
```
Prompt the user to enter a positive number which is then converted in an integer and stored in the number variable.
```python
number = int(input("Please Enter a positive number: "))
```
A first while loop is used to ensure that the user enters a positive number If the number entered is less than or equal to 0, the loop will execute and prompt the user to enter a positive number again.
````python
while number <=0:
    print("You didn't enter a positive number!")
    number = int(input("Please Enter a positive number: "))
````
A second while loop is executed until the number 1 is reached.

````python
while number != 1:
````
If the number is [even](https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/.), it is divided by 2 and the result is stored in the number variable. 
````python
    if (number%2) == 0:
        number = int((number / 2))                     
````
If the number is odd, multiply it by 3 and add 1, and it in the "number" variable.
````python
    else:
        number = int((number * 3 + 1))                 
````
Append the new number to the "numbers" list.
````python
    numbers.append(number)             
````
Print with a for loop the sequence of numbers generated by the calculation.
````python
for n in numbers:
    print(n, end= " ")            
````
</p>
</details>

- - - -
<details>
           <summary>Sources</summary>
           <p>

- [Python Program to Check if a Number is Odd or Even](https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/)
- [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
- [Python While Loops 2](https://www.programiz.com/python-programming/while-loop)
- [How to use multiple while loops at the same time?](https://stackoverflow.com/questions/43356309/how-to-use-multiple-while-loops-at-the-same-time)

</p>
</details>

### Task Week 5 - weekday.py

#### Description 

<details>
    <summary>Task requested:</summary>
           <p>

>Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
>An example of running this program on a Thursday is given below.

```sh
$ python weekday.py
Yes, unfortunately today is a weekday.
```
>An example of running it on a Saturday is as follows:

```sh
$ python weekday.py
It is the weekend, yay!
```
</p>
</details>

- - - -
The Weekday Checker is a Python program that checks whether today is a weekday or the weekend, and prints a message indicating which one it is. When run, the program prints the message "Yes, unfortunately today is a weekday." in red if today is a weekday, or "It is the weekend, yay!" in red if today is the weekend.

#### How it works

Here the main steps of the program:

1. The program can be run by executing the **"weekday.py"** script
2. Import the datetime module and the termcolor module
3. Use the datetime.datetime.today() function to get the current date and time
4. Use the weekday() function to get the current day of the week, where Monday is 0 and Sunday is 6.
5. Check whether the current day of the week is less than 5 using an if statement.
6. If the current day of the week is less than 5, print the message "Yes, unfortunately today is a weekday." in red 
7. If the current day of the week is 5 or 6 (i.e., the weekend), print the message "It is the weekend, yay!" in red.

<details>
           <summary>Code comments</summary>
           <p>

Import datatime for working with data and time.
```python
import datetime
```
Import termocolor-cprint from printing colored text.
```python
from termcolor import cprint
```
Determine the [current day of the week](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python). This code used the **'today()'** method of the **'datatime()'** class to get the current date and time, and the **'weekday()** method to extract the of the week as an integer. 0-5 is Monday-Friday (week days) and 5-6 are Saturday-Sunday (weekend days).
````python
weekno = datetime.datetime.today().weekday()
````
This code print the appropriate message based on the day of the week. The if statement check whether **'weekno'** is less than 5, which means it is a weekday (Monday-friday). the script prints the message **"Yes, unfortunately today is a weekday."** in red color using the [cprint](https://www.geeksforgeeks.org/print-colors-python-terminal/) function. Otherwise, if **'weekno'** is 5 or 6, the script prints the message **"It is the weekend, yay!"** in red color using cprint.


</p>
</details>

- - - -
<details>
           <summary>Sources</summary>
           <p>

- [how to find current day is weekday or weekends in Python?](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python)
- [Python datetime](https://www.programiz.com/python-programming/datetime)
- [weekday() Function Of Datetime.date Class In Python](https://www.geeksforgeeks.org/weekday-function-of-datetime-date-class-in-python/)
- [Print Colors in Python terminal](https://www.geeksforgeeks.org/print-colors-python-terminal/)

</p>
</details>

- - - -
    

### Task Week  6 - squareroot.py

#### Description 

<details>
           <summary>Task requested:</summary>
           <p>

>Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).
I suggest that you look at the newton method at estimating square roots.

```sh
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.
```
</p>
</details>

- - - -
In addiction to the requested task, The program is first checking that the user enter a positive number. If the number entered is negative the program propose several scenarios until the user input a positive number.

In summary, the program prompts the user to enter a positive floating-point number, and then calculates the square root of that number using the Newton method. If the user enters a negative number, the program calls a function called choice_user() to handle the case and prompt the user to either keep the same number and make it positive or enter a new positive number. Then, the program then calls the sqrt() function to calculate the square root of the number using the Newton method, and prints the result.

#### How it work

Here the main steps of the program:

1. The program can be run by executing the **"squareroot.py"** script
2. It prompt the user to enter a positive floating-point number.
3. Define a function called **choice_user()** to handle the case where the input number is negative.
4. Define a function called **sqrt() to** calculate the square root of a number using the Newton method.
5. If the input number is negative, call **choice_user()** to prompt the user to either keep the same number and make it positive or enter a new positive number.
6. Call **sqrt()** function to calculate the square root of the input number using the Newton method.
7. Print the result of the square root calculation.

<details>
           <summary>Code comments</summary>
           <p>

Prompt the user to input a positive-floating number and assign the input value to the **'user_input'** variables. 
               
```python
user_input=float(input("Please enter a positive float number "))
```
Define a function called **choice_user()**. The function is called when the input number is not positive. This function, in case the user entered a negative number, give to him two choices.
               
```python
def choice_user():
        print("You didn't enter a postive numer")
        print("\t Select what do you want to do: ")
        print("\t\t(a) keep the same number but make it positive")
        print("\t\t(b) enter a new number")
        choice = input("Enter your choice : ")
```
If the user choose option "a", make the number positive and return it.

```python
if choice == "a":
            new_number = abs(user_input)
            print (f"The new number is {new_number}")
            return new_number
```
If the user choose option "b", prompt the user to enter a new positive number

```python
else:
            return float(input("Please enter a positive float number "))
````

Define a function called **sqrt()**. This function calculate the square root of a number using the [Newton-Raphson method](http://www.andreamarino.it/python/thinkcspy/MoreAboutIteration/Newton'sMethod.html):
- The initial guess is set to half of the user input.
- A better approximation is calculated using the formula: better = 0.5 * (approx + user_input/approx)
- A loop is run until the better approximation is equal to the previous approximation
- Finally, the final aproximation is returned (the square root)

```python
def sqrt(user_input):
    approx = 0.5 * user_input
    better = 0.5 * (approx + user_input/approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + user_input/approx)
    return approx
```
This is the main program where each function is recalled if needed.
As long us **'user_input'** is less than 0 the **'choice_user()'** function will run. The output will be a positive float number, which will be passes into the **sqrt()** function to calculate its square root.Finally, the square root will be printed with a round of one digit with a mengful message.
```python
while user_input < 0:
    user_input = choice_user()
    
square_root = round(sqrt(user_input),1)
print(f'The square rot of {user_input} is approx. {square_root}')
```
</p>
</details>

- - - -
<details>
           <summary>Sources</summary>
           <p>

- [Metodo delle tangenti](https://it.wikipedia.org/wiki/Metodo_delle_tangenti)
- [La radice quadrata di 2 (metodo di Newton)](http://numerici.mateweb.eu/equazioni/radice2_newton.html#:~:text=Come%20esempio%20di%20applicazione%20del%20metodo%20di%20Newton%2C,1%20e%20a%20partire%20da%20zero%20%28tabella%20accanto%29)
- [Il Metodo di Newton](http://www.andreamarino.it/python/thinkcspy/MoreAboutIteration/Newton'sMethod.html)
- [Evoluzione calcolo radice quadrata metodo di Newton
In questa piccola guida voglio pa](https://codinglife.blog/netwon)
- [Newton-Raphson Method | Numerical Computing in Python](https://www.youtube.com/watch?v=szQUIRPrAgQ)
- [Square Root of a Number using Newton's Method | Python | The Last Minute Professor](https://www.youtube.com/watch?v=xdlIFw5EM4w)               
</p>
</details>

- - - -

### Task Week 7 - es.py

#### Description 

<details>
    <summary>Task requested:</summary>
           <p>

>Write a program that reads in a text file and outputs the number of e's it contains. 
>The program should take the filename from an argument on the command line. 

```sh
$ python es.py moby-dick.txt
116960
```
</p>
</details>

- - - -
**Script modified after lecture feedback**

The program reads a text file called by the user through the command prompt and returns the number of times the letters 'e' and/or 'E' appears in the file. Based on the exercise description, the program should be named es.py, and the file to be analyzed should be moby-dick.txt.

As an additional functionality, I have added a feature that informs the user if he forgot to prompt the file in the command line argument or if the file entered doesn't exist. 

#### How it works

Here the main steps of the program:

1. The program can be run by executing the **es.py** script.
2. The script retrieves the filename to be analyzed through the command line arguments using **sys.argv**.
3. If no filename is provided, the program exits with an error message.
4. The program then checks if the file exists in the current directory. If the file does not exist, the program informs the user that the file does not exist and either needs to be created or the spelling needs to be checked.
5. If the program finds the file, it prompts the user to enter their choice for which letter to count (lowercase "e", uppercase "E", or both).
6. It counts the number of occurrences of the chosen letter(s) in the file based on user input by calling the appropriate functions. If the user enter an invalid option He will need to enter it again.
7. Finally, the program prints the count of the chosen letter(s) occurrences in the file.

<details>
           <summary>Code comments</summary>
           <p>

import modules needed for the script:
 - import sys in order to facilitate the command line arguments 
 - import os for checking if the file exist

```python
import sys 
import os 
```
First some funtions are defined. 
Define the function **count_letter_e()**. The function counts the occurence of the letter **e** in the selected file.
Here the main steps:
   1. Open the file in read mode using the with open() statement.
   2. Read the contents of the file into a variable called counter.
   3. Count the occurrences of the uppercase letter in the file using the count() method.
   4. Return the count of occurrences as the function's result.

````python
def count_letter_e(filename, letter):
    with open(filename, "r") as f:
        counter = f.read()
        count = counter.count(letter)
    return (count)
````
Establish the variable "letter" as the letter that will be counted.
````python
letter = "e"
````
Define the function **count_letter_E()**. The function counts the occurence of the letter **E** in the selected file.
The main difference with the **count_letter_e()** function is that at the beginning it converts the input letter to uppercase using the [upper()](https://stackoverflow.com/questions/51816880/python-read-a-text-file-and-convert-it-to-upper-case-and-write-to-a-second-fi) method. 
               
````python
def count_letter_E(filename, letter):
    letter_upper = letter.upper()
    with open(filename, "r") as f:
        counter = f.read()
        count = counter.count(letter_upper)
    return (count)
````
Define the function count_letter_e_and_E(). The function counts the occurrences of both the letters 'e' and 'E' in the selected file. The main difference between this function and the count_letter_e() function is that it converts the contents of counter to lowercase using the lower() method. This means that all the letters in the file are converted to lowercase before counting the occurrences of the lowercase letter 'e'. As a result, this function counts both uppercase and lowercase 'e' occurrences in a case-insensitive manner.
               
````python
def count_letter_e_and_E(filename, letter):
    with open(filename, "r") as f:
        counter = f.read().lower()
        count = counter.count(letter)
    return (count)
````
Define the function user_choice_input().
The function displays a menu to the user with three options for counting occurrences of letters. It then prompts the user to input their choice by entering a corresponding number. Finally, the function returns the user's choice as an integer value.
               
````python
def user_choice_input():
    print (" What do you want to count: ")
    print("\t 1. e (lower case)")
    print("\t 2. E (upper case)")
    print("\t 3. e and E")
    user_choice = int(input("Please make your choice: ")) 
    return user_choice
````
Now we are entering in the main program.
First, it get the filename from the command line argument and uses a [try-except block](https://itecnote.com/tecnote/python-checking-if-sys-argvx-is-defined/) to handle the case where the user does not provide a filename as a command line argument. If no argument is provided, the script exits using the sys.exit() with an error message.

```python
try:
    filename = sys.argv[1]
except IndexError:
    sys.exit ("You didn't enter any file name. Please execute the script again")
```
It checks if the specified file does not exist using the os.path.exists() function. If the file does not exist, it terminates the script using the sys.exit() function and displaying an error message.
If the file exists, it calls the user_choice_input() function to get the user's choice for counting occurrences.
               
```python
if not os.path.exists(filename):
    sys.exit(filename + "does not exist, create it or check your spelling ")
else:
    user_choice = user_choice_input()
```
Establish the variable "letter" as the letter that will be counted.
````python
letter = "e"
````         
               
Establish the variable "letter" as a default value.
````python
letter = "e"
````             
Main program:
  1. Check if the file exist with **os.path.exist** and if not exist inform the user 
  2. if the file exist execute the above function in order to count the number of tyme variable "letters" is in the text file

````python
if not os.path.exists(filename):
    print(filename, "does not exist, create it or check your spelling ")
else:
    print(count_letter(filename, letter))           
            
````
It defines a list of valid options [1,2,3] for the user's choice and  It uses a while loop to repeatedly prompt the user for a choice until a valid option is entered.
````python
options = [1,2,3]
while user_choice not in options:
    print( "Please enter a choice between 1, 2 or 3")
    user_choice = int(input("Please make your choice: "))                    
````
It uses an if statement to call a specific function based on the user's choice. Basically, depending on the option selected by the user, the program executes a specific count.
````python
 if user_choice == 1:
    count =  count_letter_e(filename, letter)
    letter = "e"
elif user_choice == 2:
    count = count_letter_E(filename, letter)
    letter = "E"
else:
    count =count_letter_e_and_E(filename, letter)
    letter = "e and E"             
````               

It print the result of the count.
````python
print (f'In the file there are {count} letters {letter}' )                  
````
</p>
</details>

- - - -
<details>
           <summary>Sources</summary>
           <p>

-	Stackoverflow
    [Phyton command line arguments file name ](https://stackoverflow.com/questions/33766029/python-command-line-arguments-file-name)
    [How to write a function that takes in the name of a file as the argument in phyton  ](https://stackoverflow.com/questions/63066948/how-to-write-a-function-that-takes-in-the-name-of-a-file-as-the-argument-in-pyth)
    [I want to read in a file from the command line in python](https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python)
    [Python :- Read a text file and convert it to upper case and write to a second file](https://stackoverflow.com/questions/51816880/python-read-a-text-file-and-convert-it-to-upper-case-and-write-to-a-second-fi)
- youtube 
    [Python 3 Programming Tutorial - Sys Module](https://www.youtube.com/watch?v=rLG7Tz6db0w)
    [Command line arguments](https://www.youtube.com/watch?v=PZN7vVxeh9M)

- [Python Command-Line Arguments](https://realpython.com/python-command-line-arguments/)
- [Python - Command Line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.ht)
- [Count the number of times a letter appears in a text file in Python](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/)
- [Python – Checking if sys.argv[x] is defined](https://itecnote.com/tecnote/python-checking-if-sys-argvx-is-defined/)
- [Exit a Process with sys.exit() in Python](https://superfastpython.com/exit-process/)
- [Python exit command](https://pythonguides.com/python-exit-command/)
- [4 Ways of Exiting the Program with Python Exit Function](https://www.pythonpool.com/python-exit/)               
    
</p>
</details>

- - - -
### Task Week 8 - plottask.py

#### Description 

<details>
    <summary>Task requested:</summary>
           <p>

>Write a program called plottask.py that displays:
> - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
> - and a plot of the function  h(x)=x3 in the range [0, 10], 
>
> on the one set of axes.
</p>
</details>

- - - -
The code generates a histogram of random values drawn from a normal distribution and plots the function h(x) = x^3 on the same graph.
It sets the parameters for the normal distribution, generates random values, plots the histogram, and plots the function. Labels, title, legend, and grid are defined, and the plot is displayed.

#### How it works

Here the main steps of the program:

1. The program can be run by executing the "plottask.py" script.
2. The program first import necessary libraries
3. It sets the parameters for a normal distribution, including the mean, standard deviation, and number of values.
4. It generates random values from the normal distribution and stores them in a variable.
5. It creates a histogram of the generated values
6. It calculates the points for a mathematical function (h(x) = x^3) and plots the function on the same graph as the histogram.
7. It defines labels for the x-axis and y-axis, sets a title for the graph, and adds a legend.
8. Finally, it shows the plot.

<details>
           <summary>Code comments</summary>
           <p>


The program import two libraries. The first is **numpy** and it will be used to create random number from a normal distribution. The second, **matplotlib.pyplot**, is a library used to plot data. 
```python
import numpy as np
import matplotlib.pyplot as plt
```
The parameters for the normal distribution mean (**mean_x**), standard deviation (**std_x**) and number of value to be generated (**values_x**) are set.
```python
mean_x = 5
std_x = 2
values_x = 1000
```
Random values are generated from a normal distribution using the above parameters and the values are stored in the variable **'x'**.
````python
x = np.random.normal(loc=mean_x, scale=std_x, size=values_x)
````
Using the **matplotlib** library and histogram of the the random value is plot. The alpha of the parameters is to give to the plot a transparency, while the color of the plot is set to red. The label parameter is set to be used in the legend. 
````python
plt.hist(x, alpha=0.5, color='r', label='Normal Distribution')
````
**Numpy** is used to generate 100 equal spaced point between 0 and 10. 
````python
x_points = np.linspace(0, 10, 100)
````
Y point are calculated based on function h(x) = x^3
````python    
y_points = x_points ** 3              
````
Plot the funcion h(x) = x^3 with a blue color, a dotted linestyle and a label that is added that will be used in the legend.
```python
plt.plot(x_points, y_points, color='b', linestyle='dotted', label='h(x) = x^3')
```
Two fonts are defined
```python
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
```
x-axis and Y-axis are defined with font 2
````python
plt.xlabel('x - random normal number', fontdict=font2)
plt.ylabel('y = x^3', fontdict=font2)
````
The title/legend of the graph is define. I also add some grid to it.
````python
plt.title('Task Week 8', fontdict=font1)
plt.legend(loc='upper left')
plt.grid(linestyle='--', alpha=0.7)
````
Finally the plot is shown. 
````python
plt.show()                 
````
</p>
</details>

- - - -
<details>
           <summary>Sources</summary>
           <p>

- [Scipy Normal Distribution](https://pythonguides.com/scipy-normal-distribution/)
- [A Quick Introduction to Numpy Random Normal](https://www.sharpsightlabs.com/blog/numpy-random-normal/)
- [Normal (Gaussian) Distribution](https://www.w3schools.com/python/numpy/numpy_random_normal.asp)
- [How to: Plot a Function in Python](https://www.youtube.com/watch?v=ufO_BScIHDQ)
- [How to Make Attractive Matplotlib Plots in Python](https://towardsdatascience.com/customize-your-matplotlib-plots-in-python-54726f414602)
- [np.linspace(): Create Evenly or Non-Evenly Spaced Arrays](https://realpython.com/np-linspace-numpy/)
- [Histograms in Python](https://medium.com/@kasiarachuta/histograms-in-python-85bd8eaa2248)
- [Python Plotting With Matplotlib (Guide)](https://realpython.com/python-matplotlib-guide/#adding-a-legend-to-your-plot)
- [CSS Fonts](https://www.w3schools.com/css/css_font.asp)
- [Fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/font)

</p>
</details>
