# pands-problem-sheet

## Programming screepting weekly task

### General information

This document contain an explanation of every program created as weekly task during the module programming screepting. In the table of content you will be able to navigate to each single script.

### Technologies
- Python 3.19

### Table of content
* [Task week 01 Helloworld.py](https://github.com/Cecilia8989/pands-problem-sheet/edit/main/README.md#task-week-01-helloworld.py)
* [Task week 02 bank.py](https://github.com/Cecilia8989/pands-problem-sheet/edit/main/README.md#task-week-02-bank.py)
* [Task Week 03 accounts.py](https://github.com/Cecilia8989/pands-problem-sheet#task-week-03-accountspy)
* [Task Week 04 collatz.py](https://github.com/Cecilia8989/pands-problem-sheet/edit/main/README.md#task-week-04-collatzpy)

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

- The program can be run by executing the "bank.py" script. 
- The program will prompt the user to enter a first quantity in cents.
- A  second quantity in cents will be asked to the user.
- The program will them calculate the total amount in Euro by adding the two quantities and dividing the result by 100.
- The total amount in Euro will be displayed with the Euro Symbol


<details>
           <summary>Code comments</summary>
           <p>

The user is asked for two quantities in cents. The quantities need to be integer (absolute number).
```python
cents1 = int(input("Please enter an amount (in cents): "))
cents2 = int(input("Please enter an amount (in cents): "))
```
The program calculate the total amount in Euro by adding user inputs (cent1 and cent2) and dividing them by 100.
```python
amount_in_euro = (cents1 + cents2)/100

```
Print the total amount in Euro with the [Euro symbol](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python#:~:text=Euro%20is%20encoded%20as%2080h%20%280x80%29%20in%20the,as%20others%20said%2C%20using%20the%20correct%20encoding%20%28utf-8%29%3A).
````python
print (f'The sum of these is \u20ac{amount_in_euro}')
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
- The program can be run by executing the "account.py" script
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


### Task Week 04 collatz.py

#### Description
The porpuse of this script is ask to the user a positive number (if the user didn't enter a positive number it will be asked again until a positive numebr will be entered) and, depend on if the number is even or odd, have it:
 - devided per 2 ( if it is an even number).
 - moltipled * 3 and added 1 (for odd number).

Every new number will be added to a list and the full list will be printed out when the loop will be exited.

#### What the program does.
What the script do in details is:
1. it ask to the user to enter a positive number. A first while loop is used to check that the user enter a positive number. If the user enter a positive number the script will exit the first while loop and enter in the second. Otherwise, it will be asked to input a new number until this is positive.
2. Once that the script have verified that the number is positive for each number diverse by one it will check if the number is even or odd.
 - for even number it will divide the number by 2 and add it to the list "numbers"
 - for odd number it will multiply them for 3, it will add one and it will add them to the list "numbers"
3. The while loop will keep going until the number is one
4. When the number is one it will exit the second while loop and it will enter a for loop that will print all the numbers in the list "numbers".

#### Sources
- [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
- [Python While Loops 2](https://www.programiz.com/python-programming/while-loop)
- [How to use multiple while loops at the same time?](https://stackoverflow.com/questions/43356309/how-to-use-multiple-while-loops-at-the-same-time)

### Task Week  6 - Squareroot

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
In addiction to the requested task, The program is first checking that the user enter a positive number. If the number negative the program will propose several scenario until the number input by the user will be positive.

In summary, the program prompts the user to enter a positive floating-point number, and then calculates the square root of that number using the Newton method. If the user enters a negative number, the program calls a function called choice_user() to handle the case and prompt the user to either keep the same number and make it positive, or enter a new positive number. The program then calls the sqrt() function to calculate the square root of the input number using the Newton method, and prints the result.

#### How it work

Here the main steps of the program:

1. Prompt the user to enter a positive floating-point number.
2. Define a function called choice_user() to handle the case where the input number is negative.
3. Define a function called sqrt() to calculate the square root of a number using the Newton method.
4. If the input number is negative, call choice_user() to prompt the user to either keep the same number and make it positive, or enter a new positive number.
5. Call sqrt() function to calculate the square root of the input number using the Newton method.
6. Print the result of the square root calculation.

<details>
           <summary>Code comments</summary>
           <p>

Prompt the user to input a positive-floating number and assign the input value to the 'user_input' variables. 
If the user does not enter a positive number, prompt a message with 2 options and ask the user to enter their choice."

```python
user_input=float(input("Please enter a positive float number "))
```
Define a function called choice_user(). The function is called when the input number is not positive.
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
            return new_number] 
```
If the user choose option "b", prompt the user to enter a new positive number

```python
else:
            return float(input("Please enter a positive float number "))
````

Define a function called sqrt(). This function calculate the square root of a number using the Newton-Raphson method:
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
As long us 'user_input' is less than 0 the 'choice_user()' function will run. The output will be a positive 'user_input' float number that will enter in the sqrt() function that will be passes into the sqrt() function to calculate its square root.Finally, the square root will be printed with a round of 4 digits.


```python
while user_input < 0:
    user_input = choice_user()
    
square_root = sqrt(user_input)
print(round(square_root,4))
```
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

- youtube 

    [Python 3 Programming Tutorial - Sys Module](https://www.youtube.com/watch?v=rLG7Tz6db0w)
</p>
</details>

- - - -

### Task Week 7 - ES

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
The program read a file text called by the user through the prom command and return the number of time the letter "e" is in the file.
For my understanding from the explanation of the exercise the program should be called es.py and the file moby-dict.txt.
As an addiction functionality I have made the program tell to the user, in case the file doesn't exist, that the file have not been found in the directory and to create it or check the spelling.

#### How it works

The program prompts the user to input the name of a text file to be read using the sys module. The program then checks if the file exists in the current directory. If the file does not exist, the program informs the user that the file does not exist and either needs to be created or the file name needs to be checked. In this case, to meet the task requirements, a file named "moby-dick.txt" has been created in the same directory to be read by the program if specified by the user. If the program finds the file, it opens the file in read mode and counts the number of occurrences of lowercase "e" only. Finally, the program prints the count of the lowercase "e" occurrences in the file.

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
Get the filename from the user through a command line argument 

```python
filename = sys.argv[1] 
```
Establish the variable "letter" as the letter that will be counted.
````python
letter = "e"
````
Funciont that:
   1. open the file in read mode 
   2. read file contents into variable
   3. count the occurence in the the file of the variable letter
   4. return this count 

````python
def count_letter(filename, letter):
    with open(filename, "r") as f:
        counter = f.read()
        count = counter.count(letter)
    return (count)
````
Main program:
  1. Check if the file exist with os.path.exist and if not exist inform the user 
  2. if the file exist execute the above function in order to count the number of tyme variable "letters" is in the text file

````python
if not os.path.exists(filename):
    print(filename, "does not exist, create it or check your spelling ")
else:
    print(count_letter(filename, letter))           
            
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

- youtube 

    [Python 3 Programming Tutorial - Sys Module](https://www.youtube.com/watch?v=rLG7Tz6db0w)

    [Command line arguments](https://www.youtube.com/watch?v=PZN7vVxeh9M)

- Real phyton - [Python Command-Line Arguments](https://realpython.com/python-command-line-arguments/)

- Tutorialspoint - [Python - Command Line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.ht)

- Geeksforgeeks - [Count the number of times a letter appears in a text file in Python](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/)

</p>
</details>

- - - -
