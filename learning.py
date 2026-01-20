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
print(FIRST + " " + SECOND + " " + THIRD ) # TypeError: can only concatenate str (not "int") to str
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
newTitle = "the title"
print(newTitle.title()) # The Title
