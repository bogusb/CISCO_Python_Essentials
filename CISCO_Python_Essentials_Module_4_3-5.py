### MODULE 4: FUNCTIONS, TUPLES, DICTIONARIES,
### AND DATA PROCESSING

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

# 4.3. RETURNING RESULTS FROM FUNCTIONS

### 4.3.1.1 Returning a result from a function
# # Effects and results: the return instruction

# All the previously presented functions have some kind of effect -
# they produce some text and send it to the console.
#
# Of course, functions - like their mathematical siblings - may have results.
#
# To get functions to return a value (but not only for this purpose)
# you use the return instruction.
#
# This word gives you a full picture of its capabilities.
# Note: it's a Python keyword.
#
#
# The return instruction has two different variants -
# let's consider them separately.
#

# # # return without an expression
# The first consists of the keyword itself, without anything following it.
#
# When used inside a function, it causes the immediate termination of the function's execution, and an instant return (hence the name) to the point of invocation.
#
# Note: if a function is not intended to produce a result, using the return instruction is not obligatory - it will be executed implicitly at the end of the function.
#
# Anyway, you can use it to terminate a function's activities on demand, before the control reaches the function's last line.
#
# Let's consider the following function:
#
# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#
#     print("Happy New Year!")
#
#
# When invoked without any arguments:
#
# happy_new_year()
#
#
# The function causes a little noise - the output will look like this:
#
# Three...
# Two...
# One...
# Happy New Year!
# output
#
#
# Providing False as an argument:
#
# happy_new_year(False)
#
#
# will modify the function's behavior - the return instruction will cause its termination just before the wishes - this is the updated output:
#
# Three...
# Two...
# One...
# output
#
#
#
# return with an expression
# The second return variant is extended with an expression:
#
# def function():
#     return expression
#
#
# There are two consequences of using it:
#
# it causes the immediate termination of the function's execution (nothing new compared to the first variant)
# moreover, the function will evaluate the expression's value and will return (hence the name once again) it as the function's result.
# Yes, we already know - this example isn't really sophisticated:
#
# def boring_function():
#     return 123
#
# x = boring_function()
#
# print("The boring_function has returned its result. It's:", x)
#
#
# The snippet writes the following text to the console:
#
# The boring_function has returned its result. It's: 123
#
# Let's investigate it for a while.
#
# Analyze the figure below: Assigning the value returned by function to a variable
#
# The return instruction, enriched with the expression (the expression is very simple here), "transports" the expression's value to the place where the function has been invoked.
#
# The result may be freely used here, e.g., to be assigned to a variable.
#
# It may also be completely ignored and lost without a trace.
#
#
# Note, we're not being too polite here - the function returns a value, and we ignore it (we don't use it in any way):
#
# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123
#
# print("This lesson is interesting!")
# boring_function()
# print("This lesson is boring...")
#
#
# The program produces the following output:
#
# This lesson is interesting!
# 'Boredom Mode' ON.
# This lesson is boring...
# output
#
#
# Is it punishable? Not at all.
#
# The only disadvantage is that the result has been irretrievably lost.
#
# Don't forget:
#
# you are always allowed to ignore the function's result, and be satisfied with the function's effect (if the function has any)
# if a function is intended to return a useful result, it must contain the second variant of the return instruction.
# Wait a minute - does this mean that there are useless results, too? Yes - in some sense.
