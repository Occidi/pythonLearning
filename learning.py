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
