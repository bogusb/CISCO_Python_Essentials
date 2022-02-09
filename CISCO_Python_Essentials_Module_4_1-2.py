### MODULE 4: FUNCTIONS, TUPLES, DICTIONARIES,
### AND DATA PROCESSING

# 4.1. FUNCTIONS
# 4.1.1.1 Functions
# 4.1.1.2 Functions
# 4.1.1.3 Writing functions
# 4.1.1.4 Writing functions
# 4.1.1.5 Functions
# 4.1.1.6 SECTION SUMMARY
# 4.2. Function parameters and argument passing
# BACK
# 4.2. FUNCTION PARAMETERS AND ARGUMENT PASSING
# 4.2.1.1 How functions communicate with their environment
# 4.2.1.2 How functions communicate with their environment
# 4.2.1.3 How functions communicate with their environment
# 4.2.1.4 How functions communicate with their environment
# 4.2.1.5 How functions communicate with their environment
# 4.2.1.6 How functions communicate with their environment
# 4.2.1.7 How functions communicate with their environment
# 4.2.1.8 SECTION SUMMARY
# 4.3. Returning results from functions
# BACK
# 4.3. RETURNING RESULTS FROM FUNCTIONS
# 4.3.1.1 Returning a result from a function
# 4.3.1.2 Returning a result from a function
# 4.3.1.3 Returning a result from a function
# 4.3.1.4 Returning a result from a function
# 4.3.1.5 Returning a result from a function
# 4.3.1.6 LAB: A leap year: writing your own functions Lab
# 4.3.1.7 LAB: How many days: writing and using your own functions Lab
# 4.3.1.8 LAB: Day of the year: writing and using your own functions Lab
# 4.3.1.9 LAB: Prime numbers - how to find them Lab
# 4.3.1.10 LAB: Converting fuel consumption Lab
# 4.3.1.11 SECTION SUMMARY
# 4.4. Functions and scopes
# BACK
# 4.4. FUNCTIONS AND SCOPES
# 4.4.1.1 Scopes in Python
# 4.4.1.2 Scopes in Python
# 4.4.1.3 Scopes in Python | global
# 4.4.1.4 Scopes in Python
# 4.4.1.5 SECTION SUMMARY
# 4.5. Creating simple functions
# BACK
# 4.5. CREATING SIMPLE FUNCTIONS
# 4.5.1.1 Creating functions | two-parameter functions
# 4.5.1.2 Creating functions | two-parameter functions
# 4.5.1.3 Creating functions | three-parameter functions
# 4.5.1.4 Creating functions | testing triangles
# 4.5.1.5 Creating functions | right-angle triangles
# 4.5.1.6 Creating functions | factorials
# 4.5.1.7 Creating functions | Fibonacci numbers
# 4.5.1.8 Creating functions | recursion
# 4.5.1.9 SECTION SUMMARY
# 4.6. Tuples and dictionaries
# BACK
# 4.6. TUPLES AND DICTIONARIES
# 4.6.1.1 Tuples and dictionaries
# 4.6.1.2 Tuples and dictionaries
# 4.6.1.3 Tuples and dictionaries
# 4.6.1.4 Tuples and dictionaries
# 4.6.1.5 Tuples and dictionaries
# 4.6.1.6 Tuples and dictionaries | methods
# 4.6.1.7 Tuples and dictionaries | methods
# 4.6.1.8 Tuples and dictionaries
# 4.6.1.9 Tuples and dictionaries
# 4.6.1.10 SECTION SUMMARY (1/3)
# 4.6.1.11 SECTION SUMMARY (2/3)
# 4.6.1.12 SECTION SUMMARY (3/3)
# 4.7.1 Exceptions
# BACK
# 4.7.1 EXCEPTIONS
# 4.7.1.1 Exceptions
# 4.7.1.2 Exceptions
# 4.7.1.3 Exceptions (try-except)
# 4.7.1.4 Exceptions
# 4.7.1.5 Exceptions (two exceptions)
# 4.7.1.6 Exceptions | Deafult exceptions
# 4.7.1.7 Exceptions
# 4.7.1.8 Testing and debugging
# 4.7.1.9 Testing and debugging
# 4.7.1.10 Testing: bug vs. debug
# 4.7.1.11 print debugging
# 4.7.1.12 Testing and debugging – tips
# 4.7.1.13 SECTION SUMMARY
# 4.7.2.1 PROJECT: Tic-Tac-Toe Lab
# 4.7.2.2 Module Completion
# Module 4 Quiz

# Python Essentials 1: Module 4
# Functions, Tuples, Dictionaries, Exceptions, and Data Processing

# 4.1. FUNCTIONS

### 4.1.1.1 Functions
# # Why do we need functions?

'''We can now define the first condition which can help you
decide when to start writing your own functions:
if a particular fragment of the code begins to appear in more than
one place, consider the possibility of isolating it in the form of a function
invoked from the points where the original code was placed before.'''

# Możemy teraz określić pierwszy warunek, który może pomóc
# w podjęciu decyzji, kiedy zacząć pisać własne funkcje:
# jeśli dany fragment kodu zaczyna pojawiać się w więcej niż
# jednym miejscu, rozważ możliwość wyizolowania go w postaci funkcji
# wywoływanej z punktów, w których wcześniej znajdował się oryginalny kod.

'''We can now state the second condition: if a piece of code
becomes so large that reading and understating it may cause a problem,
consider dividing it into separate, smaller problems, and implement
each of them in the form of a separate function.'''

# Możemy teraz podać drugi warunek: jeśli fragment kodu
# staje się tak duży, że jego przeczytanie i zrozumienie może sprawić problem,
# rozważ podzielenie go na osobne, mniejsze problemy i zaimplementowanie
# każdego z nich w postaci osobnej funkcji.


### 4.1.1.2 Functions
# # Decomposition

'''This leads us directly to the third condition:
if you're going to divide the work among multiple programmers,
decompose the problem to allow the product to be implemented
as a set of separately written functions packed together in different modules.'''

# To prowadzi nas bezpośrednio do trzeciego warunku:
# jeśli zamierzasz podzielić pracę pomiędzy wielu programistów,
# zdekomponuj problem tak, aby produkt mógł być zaimplementowany
# jako zestaw oddzielnie napisanych funkcji spakowanych razem w różnych modułach.

### 4.1.1.3 Writing functions
# # Your first function

# print("Enter a value: ")
# a = int(input())
#
# print("Enter a value: ")
# b = int(input())
#
# print("Enter a value: ")
# c = int(input())

### 4.1.1.4 Writing functions
# # Your first function

# def my_function():
#     # function body

# def message():
#     print("Enter a value: ")
#
# print("We start here.")
# message()
# print("We end here.")

### 4.1.1.5 Functions
# # How functions work

# There are two, very important, catches.
#
# Here's the first of them:
# You mustn't invoke a function which is not known at the moment of invocation.
#
# The second catch sounds a little simpler:
# You mustn't have a function and a variable of the same name.

# print("We start here.")
#
# def message():
#     print("Enter a value: ")
#
# message()
#
# print("We end here.")


# def message():
#     print("Enter a value: ")
#
# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())


### 4.1.1.6 SECTION SUMMARY
# # Key takeaways

# You can see a complete list of Python built-in functions
# at https://docs.python.org/3/library/functions.html.

# You can define a function which takes arguments, too,
# just like the one-parameter function below:
#
# def hello(name):    # defining a function
#     print("Hello,", name)    # body of the function
#
# name = input("Enter your name: ")
# hello(name)    # calling the function


### 4.2.1.1 How functions communicate with their environment
# # Parameterized functions

# A parameter is actually a variable, but there are
# two important factors that make parameters different and special:
#
# 1. parameters exist only inside functions in which they have been defined,
# and the only place where the parameter can be defined
# is a space between a pair of parentheses in the def statement;
# 2. assigning a value to the parameter is done at the time
# of the function's invocation, by specifying the corresponding argument.

# def function(parameter):
#     ###
#
# Don't forget:
#
# - parameters live inside functions (this is their natural environment)
# - arguments exist outside functions, and are carriers of values
#   passed to corresponding parameters.
# There is a clear and unambiguous frontier between these two worlds.

# Let's now improve the function's body:
#
# def message(number):
#     print("Enter a number:", number)

# We've made use of the parameter.
# Note: we haven't assigned the parameter with any value.
# Is it correct?
# Yes, it is.
# A value for the parameter will arrive from the function's environment.

### 4.2.1.2 How functions communicate with their environment
# # Parametrized functions: continued

# def message(number):
#     print("Enter a number:", number)
#
# message() # TypeError: message() missing 1 required positional argument: 'number'

# We have to make you sensitive to one important circumstance.
# It's legal, and possible, to have a variable named the same
# as a function's parameter.
# # The snippet illustrates the phenomenon:
#
# def message(number):
#     print("Enter a number:", number)
#
# number = 1234
# message(1)
# print(number)
#
# A situation like this activates a mechanism called shadowing:
#
# parameter x shadows any variable of the same name, but...
# ... only inside the function defining the parameter.
# The parameter named number is a completely different entity
# from the variable named number.
#
# This means that the snippet above will produce the following output:
# Enter a number: 1
# 1234


### 4.2.1.3 How functions communicate with their environment
# # Parametrized functions: continued

# Let's modify the function - it has two parameters now:
#
# def message(what, number):
#     print("Enter", what, "number", number)
#
# This also means that invoking the function will require two arguments.

# def message(what, number):
#     print("Enter", what, "number", number)
#
# message("telephone", 11)
# message("price", 5)
# message("number", "number")


# This is the output you're about to see:
#
# Enter telephone number 11
# Enter price number 5
# Enter number number number

### 4.2.1.4 How functions communicate with their environment
# # Positional parameter passing

# A technique which assigns the i_th (first, second, and so on) argument
# to the i_th (first, second, and so on) function parameter
# is called positional parameter passing,
# while arguments passed in this way are named positional arguments.
#
# You've used it already, but Python can offer a lot more.
# We're going to tell you about it now.
#
# def my_function(a, b, c):
#     print(a, b, c)
#
# my_function(1, 2, 3)

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction("Luke", "Skywalker") # Hello, my name is Luke Skywalker
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")


### 4.2.1.5 How functions communicate with their environment
# # Keyword argument passing

# Python offers another convention for passing arguments,
# where the meaning of the argument is dictated by its name,
# not by its position - it's called keyword argument passing.
#
# Take a look at the snippet:
#
# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")

# Of course, you mustn't use a non-existent parameter name.
# # The following snippet will cause a runtime error:
#
# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction(surname="Skywalker", first_name="Luke")
                    # TypeError: introduction() got an unexpected keyword argument 'surname'


### 4.2.1.6 How functions communicate with their environment
# # Mixing positional and keyword arguments

# You can mix both fashions if you want -
# there is only one unbreakable rule:
# you have to put positional arguments before keyword arguments.
#
# If you think for a moment, you'll certainly guess why.
# To show you how it works, we'll use the following
# simple three-parameter function:
#
# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
#
# Its purpose is to evaluate and present the sum of all its arguments.
# The function, when invoked in the following way:
#
# adding(1, 2, 3) #   1 + 2 + 3 = 6
#
# It was - as you may suspect -
# a pure example of positional argument passing.
#
# Of course, you can replace such an invocation
# with a purely keyword variant, like this:
#
# adding(c = 1, a = 2, b = 3) #   2 + 3 + 1 = 6
#
# Note the order of the values.
#
# Let's try to mix both styles now.
# Look at the function invocation below:
#
# adding(3, c = 1, b = 2)
#
# Let's analyze it:
# the argument (3) for the a parameter is passed using the positional way;
# the arguments for c and b are specified as keyword ones.
# This is what you'll see in the console:
#
# 3 + 2 + 1 = 6
#
# Be careful, and beware of mistakes.
# If you try to pass more than one value to one argument,
# all you'll get is a runtime error.
# Look at the invocation below - it seems that we've tried to set a twice:
#
# adding(3, a = 1, b = 2)
#
# Python's response:
# TypeError: adding() got multiple values for argument 'a'
#
# Look at the snipet below. A code like this is fully correct, but it doesn't make much sense:
#
# adding(4, 3, c = 2)
#
# Everything is right, but leaving in just one keyword argument
# looks a bit weird - what do you think?


### 4.2.1.7 How functions communicate with their environment
# # Parametrized functions - more details

# It happens at times that a particular parameter's values
# are in use more often than others.
# Such arguments may have their default (predefined) values taken into
# consideration when their corresponding arguments have been omitted.
#
# They say that the most popular English last name is Smith.
# Let's try to take this into account.
#
# The default parameter's value is set using clear and pictorial syntax:
#
# def introduction(first_name, last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
#
#
# You only have to extend the parameter's name
# with the = sign, followed by the default value.
#
# Let's invoke the function as usual:
#
# introduction("James", "Doe")
#
# Can you guess the output of the program?
# Run it and check if you were right.
#
# And? Everything looks the same, but when you invoke the function
# in a way that looks a bit suspicious at first sight, like this:
#
# introduction("Henry")
#
# or this:
#
# introduction(first_name="William")
#
# there will be no error, and both invocations will succeed,
# while the console will show the following output:
#
# Hello, my name is Henry Smith
# Hello, my name is William Smith
#
# Test it.
#
# You can go further if it's useful. Both parameters
# have their default values now, look at the code below:

#
# def introduction(first_name="John", last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)

#
# This makes the following invocation absolutely valid:
#
# introduction()
#
# And this is the expected output:
#
# Hello, my name is John Smith
#
# If you use one keyword argument, the remaining one will take the default value:
#
# introduction(last_name="Hopkins")
#
# The output is:
#
# Hello, my name is John Hopkins
#
# Test it.
#
# Congratulations - you have just learned the basic ways
# of communicating with functions.

### 4.2.1.8 SECTION SUMMARY
# # Key takeaways

# 1. You can pass information to functions by using parameters. Your functions can have as many parameters as you need.
#
# An example of a one-parameter function:
#
# def hi(name):
#     print("Hi,", name)
#
# hi("Greg")
#
#
# An example of a two-parameter function:
#
# def hi_all(name_1, name_2):
#     print("Hi,", name_2)
#     print("Hi,", name_1)
#
# hi_all("Sebastian", "Konrad")
#
#
# An example of a three-parameter function:
#
# def address(street, city, postal_code):
#     print("Your address is:", street, "St.,", city, postal_code)
#
# s = input("Street: ")
# p_c = input("Postal Code: ")
# c = input("City: ")
#
# address(s, c, p_c)
#
#
# 2. You can pass arguments to a function using the following techniques:
#
# positional argument passing in which the order of arguments passed matters (Ex. 1),
# keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2),
# a mix of positional and keyword argument passing (Ex. 3).
# Ex. 1
# def subtra(a, b):
#     print(a - b)
#
# subtra(5, 2)    # outputs: 3
# subtra(2, 5)    # outputs: -3
#
#
# Ex. 2
# def subtra(a, b):
#     print(a - b)
#
# subtra(a=5, b=2)    # outputs: 3
# subtra(b=2, a=5)    # outputs: 3
#
# Ex. 3
# def subtra(a, b):
#     print(a - b)
#
# subtra(5, b=2)    # outputs: 3
# subtra(5, 2)    # outputs: 3
#
#
# It's important to remember that positional arguments mustn't follow keyword arguments. That's why if you try to run the following snippet:
#
# def subtra(a, b):
#     print(a - b)
#
# subtra(5, b=2)    # outputs: 3
# subtra(a=5, 2)    # Syntax Error
#
# Python will not let you do it by signalling a SyntaxError.

# 3. You can use the keyword argument passing technique to pre-define a value for a given argument:
#
# def name(first_name, last_name="Smith"):
#     print(first_name, last_name)
#
# name("Andy")    # outputs: Andy Smith
# name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
#
#
# Exercise 1
#
# What is the output of the following snippet?
#
# def intro(a="James Bond", b="Bond"):
#     print("My name is", b + ".", a + ".")
#
# intro()
#
# Check
# My name is Bond. James Bond.
#
#
# Exercise 2
#
# What is the output of the following snippet?
#
# def intro(a="James Bond", b="Bond"):
#     print("My name is", b + ".", a + ".")
#
# intro(b="Sean Connery")
#
# Check
# My name is Sean Connery. James Bond.
#
#
# Exercise 3
#
# What is the output of the following snippet?
#
# def intro(a, b="Bond"):
#     print("My name is", b + ".", a + ".")
#
# intro("Susan")
#
# Check
# My name is Bond. Susan.
#
#
# Exercise 4
#
# What is the output of the following snippet?
#
# def add_numbers(a, b=2, c):
#     print(a + b + c)
#
# add_numbers(a=1, c=3)
#
# Check
# SyntaxError - a non-default argument (c) follows a default argument (b=2)
#
