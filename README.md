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

### Task week 01 Helloworld.py
Helloworld.py says **Hello World!**

### Task week 02 bank.py

#### Description
This program will ask to the user 2 amounts in cents, it will sum them, will determinate the euro amount and it will print it.

#### What the program does.

1. It will ask the user to enter 2 amounts in cents (integer)
2. It will sum up the 2 amounts and will divide the sum per 100. This will dtermine the amount in Euro as integer
3. It will print "The sum of there is € {the amount}

#### Sources
- [how to write the euro sign in phyton without the keybord](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python#:~:text=Euro%20is%20encoded%20as%2080h%20%280x80%29%20in%20the,as%20others%20said%2C%20using%20the%20correct%20encoding%20%28utf-8%29%3A)
- Readme file:
  - [How to add a link or Hyperlink in Readme.MD file](https://devcracker.medium.com/how-to-add-a-link-or-hyperlink-in-readme-md-file-68752bb6499e)
  - [Manually create a Markdown table of contents for your GitHub README](https://www.setcorrect.com/portfolio/work11/)
  - [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
  - [How to write a good README for your GitHub project?](https://bulldogjob.com/readme/how-to-write-a-good-readme-for-your-github-project)
  - [How to Write a Good README File for Your GitHub Project](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
  - [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
  - [How To Write A Good README File](https://dev.to/merlos/how-to-write-a-good-readme-bog)

### Task Week 03 accounts.py

#### Description

Porpuse of this script is ask to the user an account number and output the account number with only the last 4 digits visible and the previous ones replaced by an X.

The script is dinamic, this mean the enter can enter account numbers of any length. It will read the number of digits enter by the user and it oucome all the number replaced by an X apart the last 4 digits.

#### What the program does.

What the script do in details is:
1. It calculate the number of digits entered by the user.
2. It get the last 4 digits of the account number.
3. It subtract from the total count number of the digits input by the user four digits. This will determinate the number of X that it will need to be printed.
4. It print the needed Xs and the last 4 digits of the account number.

#### Sources
- [Get the last four number of a string in phyton ](https://reactgo.com/python-get-last-four-characters/#:~:text=To%20access%20the%20last%204%20characters%20of%20a,position%20of%20a%20string.%20Here%20is%20an%20example%3A)
- [How do I print a number n times in python?](https://stackoverflow.com/questions/56091904/how-do-i-print-a-number-n-times-in-python)
- [print a variable](https://pytutorial.com/python-variable-in-string/)

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

### Task Week 7 - ES

#### Description 

Task requested:

>Write a program that reads in a text file and outputs the number of e's it contains. 
>The program should take the filename from an argument on the command line. 

```sh
$ python es.py moby-dick.txt
116960
```
The program read a file text called by the user through the prom command and return the number of time the letter "e" is in the file.
For my understanding from the explanation of the exercise the program should be called es.py and the file moby-dict.txt.
As an addiction functionality I have made the program tell to the user, in case the file doesn't exist, that the file have not been found in the directory and to create it or check the spelling.

#### Functionaly

The program prompts the user to input the name of a text file to be read using the sys module. The program then checks if the file exists in the current directory. If the file does not exist, the program informs the user that the file does not exist and either needs to be created or the file name needs to be checked. In this case, to meet the task requirements, a file named "moby-dick.txt" has been created in the same directory to be read by the program if specified by the user. If the program finds the file, it opens the file in read mode and counts the number of occurrences of lowercase "e" only. Finally, the program prints the count of the lowercase "e" occurrences in the file.

#### Code explanation 

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

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 2-bmi.py
```
User input :
```
Enter your weight in kg: 80
Enter your height in cm: 180
```
and the output is :

```
Your BMI is 24.69
```
</p>
</details>

- - - -
