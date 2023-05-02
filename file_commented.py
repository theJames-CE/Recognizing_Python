"""
    Recognizing Python Assignment-->

    The goal of this assignment is for you to use your knowledge of programming concepts and identify them in a new language.  
    There are two code snippets provided below.  One is a list of programming concepts, 
    and the other is some Python code.  In the Python file, file.py, write a comment in the same line of the code with the corresponding concept from the file.txt file.

"""

num1 = 42 # variable declaration, initialize integer
num2 = 2.3 # variable declaration, initialize float
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # array declaration, composite data type, array, initialize array of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # block structure declaration, intialize integer, initialize string, initialize boolean
fruit = ('blueberry', 'strawberry', 'banana') # tuple initialization, composite data type, tuple, tuple of primitive data type, initialize string
print(type(fruit)) # built in function, outputs value within parenthesis to console, type check, check data type, data type tuple
print(pizza_toppings[1]) # built in function, outputs value within parenthesis to console, access value of list named pizza_toppings at Index 1, 2nd position of list
pizza_toppings.append('Mushrooms') # built in method, appends value/ adds value within parenthesis to contents of list named pizza_toppings, which it is acting upon
print(person['name']) # built in function, outputs value within parenthesis to console, access's value asscoiated with key named 'name' within variable named person
person['name'] = 'George' # Changes value associated with key named 'name', within variable named person, from current value to 'George'
person['eye_color'] = 'blue' # Adds value 'blue' and asscociated key named 'eye_color' to variable named person, as a key value pair
print(fruit[2]) # built in function, outputs value within parentheses to console, access value of tuple named fruit at index 2 which is 3rd position of tuple

if num1 > 45: # Condition, If statement, compares value of variable num1 to the primitive data type, number, integer 45
    print("It's greater") # If Condition, is true, built in function will output value within parentheses
else: # Condition, else statement
    print("It's lower") # If Condition, is false, when all conditions are false built in function will output value within parentheses

if len(string) < 5: # Condition, If Statement, length Check
    print("It's a short word!") # built in function, if condition is true
elif len(string) > 15: # Condition, Elif Statement, length check
    print("It's a long word!") # built in function, elif condition is true
else: # Condition, Else Statement
    print("Just right!") # built in function, else condition when all other conditions are false

for x in range(5): # for loop, range, start 0, end 4
    print(x) # built in function, outputs value of x for every iteration of the loop
for x in range(2,5): # for loop, range, start 2, end 4
    print(x) # built in function, outputs value of x for every iteration of the loop
for x in range(2,10,3): # for loop, range, start 2, end 10, in increments of 3
    print(x) # built in function, outputs value of x for eevery iteration of loop
x = 0 # variable declaration, initializes
while(x < 5): # while loop, start at x = 0, end at x =5
    print(x)  # built in function, outputs value of x for every iteration of loop
    x += 1 # Increments the value of x by 1 for every iteration of loop

pizza_toppings.pop() # built in method, chooses index, since no argument as entered, by default it chooses -1, and removes value at default index from list, and outputs that value to the console
pizza_toppings.pop(1) # built in method, chooses value at index 1, 2nd position of list, and removes value at chosen index from list, and outputs that same value to the console

print(person) # built in function, outputs value within parentheses to the console, composite data type, variable named person
person.pop('eye_color') # built in method, chooses value associated with key named 'eye color', removes value and key from variable, and outputs the same value that was removed out to the console
print(person) # built in function, outputs value within parentheses to the console, composite data type, variable named person

for topping in pizza_toppings: # for loop, variable declaration, intialization
    if topping == 'Pepperoni': # Condition, if statement, primitive data type, initialize string
        continue    # for loop key word, continue to top of the loop and continue to run the loop, the loop continues when this condition is true, if it is false it executes the next statement line
    print('After 1st if statement') # built in function, outputs value in parentheses to console
    if topping == 'Olives': # Condition, If Statement, primitive data type, initialize string
        break # for loop key word, breaks the loop, the loop stops once this condition is true

def print_hello_ten_times(): # function, creates function with no parameters named print_hello_ten_times
    for num in range(10): # for loop, will run loop for range start at 0, end at 9, variable declaration, of variable named num, for every iteration of loop
        print('Hello') # built in function, out puts the value in parentheses to the console for every iteration of the loop

print_hello_ten_times() # function call with no arguments, executes the function named print_hello_ten_times

def print_hello_x_times(x): # function, creates function with one parameter, x, named print_hello_x_times
    for num in range(x): # for loop, will run loop for range, start at 0 and end at x minus 1, variable declaration, of variable named num, for every iteration of loop
        print('Hello') # built in function, out puts value within parentheses to the console for every iteration of the loop

print_hello_x_times(4) # function call with one argument, 4, executes the function named print_hello_x_times

def print_hello_x_or_ten_times(x = 10):  # function, creates function with one parameter, x = 10, where variable x is already declared and intialized to the value 10, 
    # but can also receive a new argument, for function  named print_hello_x_or_ten_times
    for num in range(x): # for loop, will run loop for range, start at 0 and end at 9, when no argument is entered and start at 0 and end at x minus 1 when an argument is entered, 
        # variable declaration, of variable named num, for every iteration of loop
        print('Hello') # built in function, outputs value within parentheses to the console for every iteration of the loop

print_hello_x_or_ten_times() # function call with no arguments, executes the function named print_hello_x_or_ten_times will print Hello ten times by default
print_hello_x_or_ten_times(4) # function call with one argument, 4, executes the function named print_hello_x_or_ten_times will print Hello four times


"""
Bonus section

"""

# print(num3) # - NameError: name <num3> is not defined
# num3 = 72 # variable declaration, intialization, primitive data type, number, integer
# fruit[0] = 'cranberry' # - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # - KeyError: 'favorite_team'
# print(pizza_toppings[7]) # - IndexError: list index out of range
#   print(boolean) # built in function, access the value store in the variable boolean  and outputs to the console
# fruit.append('raspberry') # - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # - AttributeError: 'tuple' object has no attribute 'pop'