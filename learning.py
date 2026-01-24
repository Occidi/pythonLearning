# PYTHON LEARNING CHEATSHEET

# thats a comment

# DATA TYPES
SINGLELINE = "saying \"Hello World!\"" # use \ to escape quotes
MULTILINE = """Test
12
3"""
AGE = 32
BOOLEAN = True

# Set: An unordered collection of unique elements
a_set_var = {7, 5, 8}

# Dictionary: A collection of key-value pairs enclosed in curly braces
a_dictionnary = {'name': 'Alice', 'age': 25}

# Tuple: An immutable ordered collection, enclosed in brackets
my_tuple_var = (7, "test", 8)

# Range: A sequence of numbers, often used in loops
my_range_var = range(5)

# List: An ordered collection of elements that supports different data types.
my_list = [22, 'Hello world', 3.14, True]

# None: A special value that represents the absence of a value.
my_none_var = None

print( "Hello World", "1", "2") # Hello World 1 2
print(type(my_tuple_var)) # <class 'tuple'>
isinstance(my_tuple_var, tuple) # True

# STRING FUNCTIONS

print('Hello' in SINGLELINE)  # True (checks if string includes hello )
print(len(SINGLELINE))  # 21 (checks for string length)
print(SINGLELINE[0])  # s
print(SINGLELINE[-1])  # "

# Strings (and integer, float, boolean, tuple, and range) are immutable data types in Python.
# This means that you can reassign a different string to a variable
# But direct modification of a string isn't allowed:
greeting = 'hi'
# greeting[0] = 'H' # TypeError: 'str' object does not support item assign

# string concatenation !! only between strings (need to convert to string if needed)
FIRST = "First"
SECOND = "second"
THIRD = 3
print(FIRST + " " + SECOND) # First second
# print(FIRST + " " + SECOND + " " + THIRD ) # TypeError: can only concatenate str (not "int") to str
print(FIRST + " " + SECOND + " " + str(THIRD)) # First second 3

#string literal aka f-strings (starts with f"")
num1 = 5
num2 = 10
print(f"The sum of {num1} and {num2} is {num1 + num2}") # The sum of 5 and 10 is 15

print(FIRST[2:4]) # rs string[start:stop] both can be omitted if needed, a third param for steps can be added
print(FIRST[::-1]) # tsriF (reversed "First" due to the -1 step)

# STRING METHODS
print(FIRST.upper()) # FIRST
print(FIRST.lower()) # first
leadingtrailing = " test 123 "
print(leadingtrailing.strip()) # test 123
print(leadingtrailing.replace("te", "vo")) # vost 123
print(leadingtrailing.split()) # ['test', '123']
my_list = ['hello', 'world']
print(FIRST.join(my_list)) # hellofirstworld / join(iterable): Joins elements of an iterable into a string with a separator.
print(FIRST.startswith("FI")) # False
print(FIRST.startswith("Fi")) # True
print(FIRST.endswith("st")) # True
print(FIRST.find("rst")) # 2
print(FIRST.find("tsr")) # -1
print(leadingtrailing.count("t")) # 2
print(SECOND.capitalize()) # Second
print(SECOND.isupper()) # False
print(SECOND.upper().isupper()) # True
print(FIRST.islower()) # False
print(FIRST.lower().islower()) # True
NEWTITLE = "the title"
print(NEWTITLE.title()) # The Title


# NUMBERS AND MATHS

my_int = 10
print(type(my_int)) # <class 'int'>
my_neg_int = -5

sum_ints = my_int + my_neg_int  # 5
sub_ints = my_int - my_neg_int # 15
multi_ints = my_int * my_neg_int # -50
div_ints = my_int / my_neg_int # -2

my_float = 12.0
my_neg_float = -4.9

print(type(my_float)) # <class 'float'>

# operation with both ints and float result in float
sum_int_and_float = my_int + my_float # 22.0
print(type(sum_int_and_float)) # <class 'float'>

mod_ints = my_int % my_neg_int # 0
mod_floats = my_float % my_neg_float # -2.700000000000001

#Floor division divides two numbers and returns the greatest integer >= to the result
my_int_2 = 4
floor_div_ints = my_int // my_int_2 # 2

expo_int = my_int ** my_int_2 # 10000

#built in function
my_float_from_int = float(my_int)  # 10.0
my_float_from_string = float("42.0") # 42.0
print(type(my_float_from_int), type(my_float_from_string))  # <class 'float'> <class 'float'>

my_float_2 = 12.92563
my_int_from_float = int(my_float) # 12
my_int_from_string = int("42") # 42
print(type(my_int_from_float), type(my_int_from_string))  # <class 'int'> <class 'int'>

rounded_int_1 = round(my_float_2) # 13
rounded_int_2 = round(my_float_2, 1) # 12.9

# abs returns the absolute value of a number,
num = -15
absolute_value = abs(num) # 15


# pow raises a number to the power of another or performs modular exponentiation.
result_1 = pow(2, 3)  # Equivalent to 2 ** 3 = 8
result_2 = pow(2, 3, 5)  # (2 ** 3) % 5 = 3

#assignement operators
my_var = 10
my_var += 5 # equivalent to my_var = my_var + 5 // 15
my_var -= 3 # 12
my_var *= 2 # 24
my_var /= 2 # 12.0
my_var //= 5 # 2.0
my_var %= 2 # 0.0
new_var = 10
new_var **= 3 # 1000

# can use + and * operators on strings (other throw TypeError)
greet = 'Hello'
greet += ' World'
print(greet) # Hello World

greet = 'Hello'
greet *= 3
print(greet) # HelloHelloHello

# increment (there is no my_var++ or ++my_var)
my_var = 5
my_var += 1
print(my_var) # 6

# BOOLEANS AND CONDITIONALS

print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

AGE = 12
if AGE >= 18:
    print("You are an adult")
elif AGE >= 13:
    print("You are still a lil baby")
else:
    print("wait you are an actual baby")

# in Python, code blocks are determined by indentation (usually 4 spaces)
#if age >= 18:
#print('You are an adult') # IndentationError

# truthy falsy values
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

# boolean operators

is_citizen = True
AGE = 25
print(is_citizen and AGE) # 25 / similar to how && works in JS
if is_citizen and AGE >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

is_employed = False
print(AGE or is_employed) # 25 / similar to how || works in JS

is_student = True
if AGE < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

# not operator same as ! in JS

is_admin = False
if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')


# SCOPE AND FUNCTIONS

name = input('What is your name?') # User types "xdd" and presses Enter  
print('Hello', name) # Output: Hello xdd

print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

# need indentation similar to if statement blocks
def hello():
    print('Hello World Function')
hello()

def calculate_sum(a, b):
    print(a + b)
my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None / with no return statement, a function return None by default
# calculate_sum() # TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'

def proper_calculate_sum(a, b):
    return a + b
my_sum = proper_calculate_sum(3, 1) # 4
print(my_sum) # 4

# local scope
def my_func():
    my_function_var = 10
    print(my_function_var)
my_func() # 10
# print(my_function_var) # NameError: name 'my_var' is not defined

# enclosing scope
def outer_func():
    msg = 'Hello there!'
    # print(res) # NameError: name 'res' is not defined
    def inner_func():
        res= "local scope var"
        print(msg)

    inner_func()

outer_func() # Hello there!

def outer_func_2():
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
    inner_func()
    print(res)  # Now res is accessible and modified

outer_func_2()

# global scope
my_global_var = 100

def show_var():
    global my_made_global_var
    my_made_global_var = 7
    print(my_global_var, my_made_global_var)

show_var() # 100 7
print(my_global_var) # 100

a_global_var = 10

def change_var():
    global a_global_var  # Allows modification of a global variable
    a_global_var = 20

change_var()
print(a_global_var)  # now modified globally to 20

# built in scope
# functions like str() type() isinstance() that are available everywhere