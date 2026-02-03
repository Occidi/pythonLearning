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

# LOOPS AND SEQUENCES

# Lists

cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # 'Los Angeles'
cities[-1] # 'Tokyo'
name = "test"
namelist = list(name) # ['t', 'e', 's', 't']
len(namelist) # 4
namelist[0] = "a" # ['a', 'e', 's', 't']
del namelist[0] # ['e', 's', 't']
"s" in namelist # True

developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer # similar to js destructuring
name, *rest = developer # name = "Alice" and rest = [34, 'Rust Developer']]

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
somenumbers = [7,8]
numbers.extend(somenumbers) # [1, 2, 3, 4, 5, 6, 7, 8 ]
numbers.insert(2, 2.5) # [1, 2, 2.5, 3, 4, 5, 6, 7, 8 ]
numbers.remove(2.5) # [1, 2, 3, 4, 5, 6, 7, 8 ] // this will only remove the first occurence
numbers.pop(0) # 1 is removed
numbers.clear() # []
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers) # [1, 2, 19, 35, 41, 67]
numbers.sort() # [1, 2, 19, 35, 41, 67] same thing but mutate the list directly
numbers.reverse() # [67, 41,35,19, 2,1]
numbers.index(19) # 3

# Tuples
# data type used to create an ordered sequence of values. Tuples can contain a mixed set of data types like this:
# while lists are a mutable data type, tuples are immutable

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2
sorted(programming_languages, key=len) # ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

# Loops

for language in programming_languages:
    if language == 'Python':
        break
    if language == 'Java':
        continue
    print(language)

for char in 'code':
    print(char)

final = 3
guess = 0

while guess != final:
    guess += 1

# Range
# used to generate a sequence of integers
# range(start, stop, step) // stop is required, only accepts integers
for num in range(3):
    print(num) # prints 0 -> 1 -> 2 as 3 is the required stop arg which is noninclusive from a 0 starting range

# a list of even integers between 2 and 10:
numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]

#Enumerate 
# keeps track of the index for an iterable and returns an enumerate object.
languages = ['Spanish', 'English', 'Russian', 'Chinese']
list(enumerate(languages)) # [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}') # Index 0 and language Spanish etc

# if you need to iterate over multiple iterables in parallel use zip() which combines lists into pairs of elements and returns an iterator of tuples.
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]
list(zip(developers, ids)) # [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')

even_numbers = []
for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

# List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets.
even_numbers = [num for num in range(21) if num % 2 == 0]

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
def is_long_word(word):
    return len(word) > 4
long_words = list(filter(is_long_word, words)) # ['mountain', 'river', 'cloud']

celsius = [0, 10, 20, 30, 40]
def to_fahrenheit(temp):
    return (temp * 9/5) + 32
fahrenheit = list(map(to_fahrenheit, celsius)) # [32.0, 50.0, 68.0, 86.0, 104.0]

numbers = [5, 10, 15, 20]
total = sum(numbers) # Result: 50

# lambda function
# great when you need to use them in higher order functions
lambda num: num ** 2 # anonymous square function

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # [2, 4]

# important to be aware of best practices. not a good practice to assign a lambda function to a variable
# square = lambda x: x ** 2
# defeats the purpose of using anonymous functions
# they are best used as very simple inline function, otherwise a regular function with def is best


# DICTIONNARY AND SET

# Keys must be unique and immutable data type. However, the values can be repeated, and they can be of any data type.
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

pizza['name'] # 'Margherita Pizza'
# To update a value,add the assignment operator, followed by the new value.
# If the key doesn't exist in the dictionary, a new key-value pair will be created
pizza['name'] = 'Margherita'
print(pizza['name']) # 'Margherita'

# dictionary.get(key, default)
pizza.get('toppings', []) # ['mozzarella', 'basil'] // if toppings didnt exist it would return the empty list instead of an error

pizza.keys() # dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])
pizza.values() # dict_values(['Margherita Pizza', 8.9, 250, ['mozzarella', 'basil']])
pizza.items() # dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
# pizza.clear()
# pizza.pop('price', 10) # second arg is needed default value otherwise throws error
#Python 3.7 and more recent versions, the .popitem() method removes the last inserted item:
pizza.popitem()
pizza.update({ 'price': 15, 'total_time': 25 }) # {'name': 'Margherita Pizza', 'price': 15,'calories_per_slice': 250,'total_time': 25 }

#looping over dictionnaries some example
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
for price in products.values():
    print(price)

for product, price in products.items():
    print(product, price)

# Sets
# don't store duplicate values. If you try to add a duplicate value to a set, only one of them will be stored.
# mutable and unordered, cannot use indices or keys to access them. 
# only contain values of immutable data types like numbers, strings, and tuples. 
# support mathematical set operations, including union, intersection, difference, and symmetric difference.
my_set = {1, 2, 3, 4, 5} 
set() # Set
{}    # Dictionary
my_set.add(6) # {1, 2, 3, 4, 5, 6}
my_set.add(5) # {1, 2, 3, 4, 5, 6}
my_set.remove(4) # raise an error if not found
my_set.discard(4)
my_set.clear()

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}
print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False
print(my_set.isdisjoint(your_set)) # False
my_set | your_set # {1, 2, 3, 4, 5, 6}
my_set & your_set # {2, 3, 4}
my_set - your_set # {1, 5}
my_set ^ your_set # {1, 5, 6}
my_set -= your_set
print(my_set) # {1, 5}
print(5 in my_set) # True


# Modules

# import module_name
import math as m
m.sqrt(36)

# from math import radians, sin, cos

# CLASSES AND OBJECTS

# a class is the template or the blueprint, and an object is what is created using that template.
# a class defines what data and behavior the object should have, and an object holds the actual data and uses that behavior.
# write a class once, and you can make many objects from it, each with different data.

class ClassName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    classAttribute = "test"

    def sample_method(self):
        print(self.name.upper())

object1 = ClassName("name", 21)
object2 = ClassName("namez", 22)
object1.sample_method() # NAME
object2.sample_method() # NAMEZ

ClassName.classAttribute # "test"
object1.classAttribute # "test"

# when you create your own class, Python won't know how to handle things automatically. like calling len(object1) will throw
# if you want to use those methods you have to redefine them in your class like
# def __len__(self):
#       return self.age


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John Doe', 30)
print(getattr(person, 'name')) # John Doe
print(getattr(person, 'age')) # 30
print(getattr(person, 'city', 'Milano')) # Milano

attr_name = input('Enter the attribute you want to see: ') # if the user types in name, they see John Doe, and if they type in age, they see 30.
print(getattr(person, attr_name, 'Attribute not found')) # if they type something that doesn't exist in the class like email, they see Attribute not found.

# setattr(object, attribute_name, value)
# hasattr(object, attribute_name)
# delattr(object, attribute_name)