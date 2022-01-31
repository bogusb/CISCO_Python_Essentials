# MODULE 3: BOOLEAN VALUES, CONDITIONAL EXECUTION,
# LOOPS, LISTS AND LIST PROCESSING,
# LOGICAL AND BITWISE OPERATIONS

# 3.1. COMPARISON OPERATORS AND CONDITIONAL EXECUTION
# Python Essentials 1: Module 3
# 3.1.1.1 Making decisions in Python
# 3.1.1.2 Making decisions in Python
# 3.1.1.3 Making decisions in Python
# 3.1.1.4 LAB: Questions and answers Lab
# 3.1.1.5 Making decisions in Python
# 3.1.1.6 Making decisions in Python
# 3.1.1.7 Making decisions in Python
# 3.1.1.8 Making decisions in Python
# 3.1.1.9 Making decisions in Python
# 3.1.1.10 LAB: Comparison operators and conditional execution Lab
# 3.1.1.11 LAB: Essentials of the if-else statement Lab
# 3.1.1.12 LAB: Essentials of the if-elif-else statement Lab
# 3.1.1.13 SECTION SUMMARY (1/2)
# 3.1.1.14 SECTION SUMMARY (2/2)

# 3.2. LOOPS
# 3.2.1.1 Loops in Python | while
# 3.2.1.2 Loops in Python | while
# 3.2.1.3 LAB: Essentials of the while loop - Guess the secret number Lab
# 3.2.1.4 Loops in Python | for
# 3.2.1.5 Loops in Python | for
# 3.2.1.6 LAB: Essentials of the for loop - counting mississippily Lab
# 3.2.1.7 Loop control in Python | break and continue
# 3.2.1.8 Loop control in Python | break and continue
# 3.2.1.9 LAB: The break statement - Stuck in a loop Lab
# 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater Lab
# 3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater Lab
# 3.2.1.12 Python loops | else
# 3.2.1.13 Python loops | else
# 3.2.1.14 LAB: Essentials of the while loop Lab
# 3.2.1.15 LAB: Collatz's hypothesis Lab
# 3.2.1.16 SECTION SUMMARY (1/2)
# 3.2.1.17 SECTION SUMMARY (2/2)

# ----------------------------------------

# var = 0  # Assigning 0 to var
# print(var != 0)
#
# var = 1  # Assigning 1 to var
# print(var != 0)

# 3.1.1.4 LAB: Questions and answers
# n = int(input("n : "))
# print("False" * (n < 100), "True" * (n >= 100), sep="")

# 3.1.1.8 Making decisions in Python
# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
# Print the result
# print("The larger number is:", larger_number)

# # Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1
#
# # We check if the second number is larger than current largest_number
# # and update largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2
#
# # We check if the third number is larger than current largest_number
# # and update largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3
#
# # Print the result
# print("The largest number is:", largest_number)

# Przerobiony na pary liczb.
# if number1 > number2:
#     if number1 > number3:
#         largest_number = number1
#     else:
#         largest_number = number3
# else:
#     if number2 > number3:
#         largest_number = number2
#     else:
#         largest_number = number3
# # Print the result
# print("The largest number is:", largest_number)
#
# Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

# largest_number = max(number1, number2, number3)

# Print the result.
# print("The largest number is:", largest_number)

# 3.1.1.10 LAB: Comparison operators and conditional execution
# _input = input("Input your favorite indoor houseplant : ")
# if _input == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif _input == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print(f"Spathiphyllum! Not {_input}!")
#

# 3.1.1.11 LAB: Essentials of the if-else statement
# income = float(input("Enter the annual income: "))
# high_income = 85528.0
# tax_relief = 556.02
# # 2 scenariusze naliczenia zalezne od przychodu
# if income <= high_income:
#     tax = income * 0.18 - tax_relief
# else:
#     tax = 14839.02 + 0.32 * (income - high_income) #surplus
#
# # podatek ujemny
# if tax < 0:
#     tax = 0
#
# # wydruk
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

# 3.1.1.12 LAB: Essentials of the if-elif-else statement
# year = int(input("Enter a year: "))
#
# if year < 1582:
#     print("Not within the Gregorian calendar period")
# else:
#     if year % 4:
#         leap_common = "Common"
#     elif year % 100:
#         leap_common = "Leap"
#     elif year % 400:
#         leap_common = "Common"
#     else:
#         leap_common = "Leap"
#     print(leap_common, "year")

# 3.1.1.14 SECTION SUMMARY (2/2)
# x, y, z = 5, 10, 8
# print(x > z)
# print((y - 5) == x)


# 3.2.1.1 Loops in Python | while
#
# # Store the current largest number here.
# largest_number = -999999999
#
# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))
#
# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))
#
# # Print the largest number.
# print("The largest number is:", largest_number)

# 3.2.1.2 Loops in Python | while
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
#
# odd_numbers = 0
# even_numbers = 0
#
# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))
#
# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))
#
# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# ------------------------------------
# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# 3.2.1.3 LAB: Essentials of the while loop - Guess the secret number
# secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# guess_number = int(input("?  "))
# while guess_number != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     guess_number = int(input("Guess the secret number again?  "))
# print("\nYes! It is this number:  << ", guess_number, " >> !!!")
# print("Well done, muggle! You are free now.")

# 3.2.1.4 Loops in Python | for
# i = 0
# while i < 100:
#     # do_something()
#     i += 1

# for i in range(100):
#     # do_something()
#     pass

# for i in range(10):
#     print("The value of i is currently", i)

# for i in range(2, 8):
#     print("The value of i is currently", i)


# for i in range(2, 8, 3):
#     print("The value of i is currently", i)


# for i in range(1, 1):
#     print("The value of i is currently", i)

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2

# 3.2.1.6 LAB: Essentials of the for loop - counting mississippily
#import time
# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
# Write a print function with the final message.

# import time
#
# for i in range (1, 6):
#     print(i, "Mississippi")
#     use: time.sleep(1)
#
# print("Ready or not, here I come!")

# # 3.2.1.7 Loop control in Python | break and continue
# # break - example
# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
# # continue - example
# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")

# largest_number = -99999999
# counter = 0
#
# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#
# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")
#
# largest_number = -99999999
# counter = 0
#
# number = int(input("Enter a number or type -1 to end program: "))
#
# while number != -1:
#     print(number, counter)
#     if number == -1:
#         continue
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))
# print("Pa", number, counter)
# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# # 3.2.1.9 LAB: The break statement - Stuck in a loop
# secret_word = "chupacabra"
# exit_word = str(input("Enter the secret exit word : "))
# while True:
#     if exit_word != secret_word:
#         exit_word = str(input("Enter the secret exit word : "))
#     else:
#         break
# print("You've successfully left the loop.")


# # 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater

# # Prompt the user to enter a word
# # and assign it to the user_word variable.
# for letter in user_word:
#     # Complete the body of the for loop.

# user_word = str(input("Enter a word : "))
# user_word = user_word.upper()
# for letter in user_word:
#     if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
#         continue
#     print(letter)

# # 3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater
#
# word_without_vowels = ""
# # Prompt the user to enter a word
# # and assign it to the user_word variable.
# for letter in user_word:
#     # Complete the body of the loop.
# # Print the word assigned to word_without_vowels.

# word_without_vowels = ""
# user_word = str(input("Enter a word : "))
# user_word = user_word.upper()
#
# for letter in user_word:
#     if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
#         continue
#     word_without_vowels += letter
#
# print(word_without_vowels)


# 3.2.1.14 LAB: Essentials of the while loop
#
# blocks = int(input("Enter the number of blocks: "))
# used_blocks = 0
# height = 0
#
# while used_blocks < blocks:
#     height += 1
#     used_blocks += height
#     if blocks < used_blocks:
#         height -= 1
#         continue
#
# print("The height of the pyramid:", height)

# # 3.2.1.15 LAB: Collatz's hypothesis
# c0 = int(input("Enter an integer > 1 : "))
# steps = 0
#
# if c0 > 1:
#     while c0 != 1:
#         steps += 1
#         if c0 % 2 == 0:
#             c0 /= 2
#         else:
#             c0 = c0 * 3 + 1
#         print(int(c0))
#     print("steps = ", steps)
# else:
#     print("Entered integer incorrect!")



# # # 3.2.1.16 SECTION SUMMARY (1/2)
# Key takeaways
#
# 1. There are two types of loops in Python: while and for:
#
# the while loop executes a statement or a set of statements as long as a specified boolean condition is true, e.g.:
#
# # Example 1
# while True:
#     print("Stuck in an infinite loop.")
#
# # Example 2
# counter = 5
# while counter > 2:
#     print(counter)
#     counter -= 1
#
#
# the for loop executes a set of statements many times; it's used to iterate over a sequence (e.g., a list, a dictionary, a tuple, or a set - you will learn about them soon) or other objects that are iterable (e.g., strings). You can use the for loop to iterate over a sequence of numbers using the built-in range function. Look at the examples below:
#
# # Example 1
# word = "Python"
# for letter in word:
#     print(letter, end="*")
#
# # Example 2
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
#
#
# 2. You can use the break and continue statements to change the flow of a loop:
#
# You use break to exit a loop, e.g.:
#
# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end="")
#
#
# You use continue to skip the current iteration, and continue with the next iteration, e.g.:
#
# text = "pyxpyxpyx"
# for letter in text:
#     if letter == "x":
#         continue
#     print(letter, end="")
#
#
#
#
#
# 3. The while and for loops can also have an else clause in Python. The else clause executes after the loop finishes its execution as long as it has not been terminated by break, e.g.:
#
# n = 0
#
# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n, "else")
#
# print()
#
# for i in range(0, 3):
#     print(i)
# else:
#     print(i, "else")
#
#
# 4. The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:
#
# start is an optional parameter specifying the starting number of the sequence (0 by default)
# stop is an optional parameter specifying the end of the sequence generated (it is not included),
# and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
# Example code:
#
# for i in range(3):
#     print(i, end=" ")  # Outputs: 0 1 2
#
# for i in range(6, 1, -2):
#     print(i, end=" ")  # Outputs: 6, 4, 2

##### 3.2.1.17 SECTION SUMMARY (2/2)
# Key takeaways: continued
# Exercise 1
#
# Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# # for i in range(1, 11):
#     # Line of code.
#         # Line of code.
# # Check
#
# for i in range(0, 11):
#     if i % 2 != 0:
#         print(i)
#
#### Exercise 2
# # Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# # x = 1
# while x < 11:
#     # Line of code.
#         # Line of code.
#     # Line of code.
# # Check
# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

###Exercise 3
# # Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:
# # for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         # Line of code.
#     # Line of code.
# # Check
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")

##Exercise 4
# Create a program with a for loop and a continue statement.
# The program should iterate over a string of digits,
# replace each 0 with x, and print the modified string to the screen.
# Use the skeleton below:
# for digit in "0165031806510":
#     if digit == "0":
#         # Line of code.
#         # Line of code.
#     # Line of code.
# Check

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

## Exercise 5
# What is the output of the following code?
# n = 3
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

## Exercise 6
# What is the output of the following code?
# n = range(4)
# for num in n:
#     print(num - 1)
# else:
#     print(num)

## Exercise 7
# What is the output of the following code?
# for i in range(0, 6, 3):
#     print(i)
