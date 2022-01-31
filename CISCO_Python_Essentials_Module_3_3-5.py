# 3.3. LOGIC AND BIT OPERATIONS IN PYTHON
# 3.3.1.1 Logic and bit operations in Python | and, or, not
# 3.3.1.2 Logic and bit operations in Python | and, or, not
# 3.3.1.3 Logic and bit operations in Python
# 3.3.1.4 Logic and bit operations in Python | Bitwise operators
# 3.3.1.5 Logic and bit operations in Python | Bit shifting Now
# 3.3.1.6 SECTION SUMMARY

# 3.4. LISTS
# 3.4.1.1 Lists - collections of data Now
# 3.4.1.2 Lists - collections of data | Indexing
# 3.4.1.3 Lists - collections of data | Indexing
# 3.4.1.4 Lists - collections of data | Operations on lists
# 3.4.1.5 Lists - collections of data | Operations on lists
# 3.4.1.6 LAB: The basics of lists Lab
# 3.4.1.7 Lists - collections of data | Functions and methods
# 3.4.1.8 Lists - collections of data | list methods
# 3.4.1.9 Lists - collections of data | list methods
# 3.4.1.10 Lists - collections of data | lists and loops
# 3.4.1.11 Lists - collections of data | lists and loops
# 3.4.1.12 Lists - collections of data | lists and loops
# 3.4.1.13 LAB: The basics of lists - the Beatles Lab
# 3.4.1.14 SECTION SUMMARY

# 3.5. SORTING SIMPLE LISTS
# 3.5.1.1 Sorting simple lists - the bubble sort algorithm
# 3.5.1.2 Sorting simple lists - the bubble sort algorithm
# 3.5.1.3 Sorting simple lists - the bubble sort algorithm
# 3.5.1.4 SECTION SUMMARY

# 3.6. LIST PROCESSING
# 3.6.1.1 Operations on lists
# 3.6.1.2 Operations on lists | slices
# 3.6.1.3 Operations on lists | slices
# 3.6.1.4 Operations on lists | slices
# 3.6.1.5 Operations on lists | slices, del
# 3.6.1.6 Operations on lists | in, not in
# 3.6.1.7 Lists - more details
# 3.6.1.8 Lists - more details
# 3.6.1.9 LAB: Operating with lists - basics Lab
# 3.6.1.10 SECTION SUMMARY

# 3.7.1 MULTIDIMENSIONAL ARRAYS
# 3.7.1.1 Lists in advanced applications
# 3.7.1.2 Lists in advanced applications | Arrays
# 3.7.1.3 Lists in advanced applications | Arrays
# 3.7.1.4 Lists in advanced applications | Arrays
# 3.7.1.5 Lists in advanced applications | Arrays
# 3.7.1.6 SECTION SUMMARY
# 3.7.1.7 Module Completion
# Module 3 Quiz Quiz


#### Module 3.3 ---
### 3.3.1.2 Logic and bit operations in Python | and, or, not

# Logical expressions
# Let's create a variable named var and assign 1 to it. The following conditions are pairwise equivalent:
# # Example 1:
# print(var > 0)
# print(not (var <= 0))
#
# # Example 2:
# print(var != 0)
# print(not (var == 0))
#
# You may be familiar with De Morgan's laws. They say that:
#
# The negation of a conjunction is the disjunction of the negations.
# The negation of a disjunction is the conjunction of the negations.
#
# Let's write the same thing using Python:
#
# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

# 3.3.1.5 Logic and bit operations in Python | Bit shifting
# var = 17
# var_right = var >> 1
# var_left = var << 2
# print(var, var_left, var_right)
#
# Note:
# 17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8
# (shifting to the right by one bit is the same as integer division by two)
# 17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68
# (shifting to the left by two bits is the same as integer multiplication by four)

### 3.3.1.6 SECTION SUMMARY
# Exercise 1
# What is the output of the following snippet?
# x = 1
# y = 0
#
# z = ((x == y) and (x == y)) or not(x == y)
# print(not(z))

# # Exercise 2
# # What is the output of the following snippet?
#
# x = 4
# y = 1
#
# a = x & y #0
# b = x | y #5
# c = ~x  # tricky! #-5
# d = x ^ 5 #1
# e = x >> 2 #1
# f = x << 2 #16
#
# print(a, b, c, d, e, f)
#
# # Check


### 3.4.1.1 Lists - collections of data
# numbers = [10, 5, 7, 2, 1]

### 3.4.1.2 Lists - collections of data | Indexing
# print("Original list content:", numbers)  # Printing original list content.
# # Indexing lists
# numbers[0] = 111
# print("New list content: ", numbers)  # Current list content.

###
# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
#
# numbers[0] = 111
# print("\nPrevious list content:", numbers)  # Printing previous list content.
#
# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("New list content:", numbers)  # Printing current list content.

###
# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
#
# numbers[0] = 111
# print("\nPrevious list content:", numbers)  # Printing previous list content.
#
# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("Previous list content:", numbers)  # Printing previous list content.
#
# print("\nList length:", len(numbers))  # Printing the list's length.
#
# ###
# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
#
# numbers[0] = 111
# print("\nPrevious list content:", numbers)  # Printing previous list content.
#
# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("Previous list content:", numbers)  # Printing previous list content.

### 3.4.1.3 Lists - collections of data | Indexing
# # Accessing list content
# # Each of the list's elements may be accessed separately. For example, it can be printed:
# print(numbers[0]) # Accessing the list's first element.
# # The len() function
# print("\nList's length:", len(numbers))  # Printing previous list length.
#
# ### 3.4.1.4 Lists - collections of data | Operations on lists
# # Removing elements from a list
# del numbers[1]  # Removing the second element from the list.
# print("New list's length:", len(numbers))  # Printing new list length.
# print("\nNew list content:", numbers)  # Printing current list content.
#
# ###

### 3.4.1.5 Lists - collections of data | Operations on lists
# # Negative indices are legal
# numbers = [111, 7, 2, 1]
# print(numbers[-1])
# print(numbers[-2])

### 3.4.1.6 LAB: The basics of lists
# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.
# # Step 2: write a line of code that removes the last element from the list.
# # Step 3: write a line of code that prints the length of the existing list.
# print(hat_list)

# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
#
# hat_list[2] = int(input("Enter a integer number : "))
# del hat_list[-1]
# print("Modified hat_list length:", len(hat_list))
#
# print(hat_list)

### 3.4.1.7 Lists - collections of data | Functions and methods
# # Functions vs. methods
# In general, a typical function invocation may look like this:
# result = function(arg)
# A typical method invocation usually looks like this:
# result = data.method(arg)

### 3.4.1.8 Lists - collections of data | list methods
# # Adding elements to a list: append() and insert()
# A new element may be glued to the end of the existing list:
# list.append(value)
# The insert() method is a bit smarter - it can add a new element at any place in the list, not only at the end.
# list.insert(location, value)
# It takes two arguments:
# the first shows the required location of the element to be inserted;
# note: all the existing elements that occupy locations to the right of the new element
# (including the one at the indicated position)
# are shifted to the right, in order to make space for the new element;
# the second is the element to be inserted.
#
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)
# ###
# numbers.append(4)
# print(len(numbers))
# print(numbers)
# ###
# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)
# ###
# # Add the following snippet after the last line of code in the editor:
# numbers.insert(1, 333)
# print(numbers)

### 3.4.1.9 Lists - collections of data | list methods
# # Adding elements to a list: continued
# You can start a list's life by making it empty
# (this is done with an empty pair of square brackets)
# and then adding new elements to it as needed.

# my_list = []  # Creating an empty list.
# for i in range(5):
#     my_list.append(i + 1)
# print(my_list) # [1, 2, 3, 4, 5]

# my_list = []  # Creating an empty list.
# for i in range(5):
#     my_list.insert(0, i + 1)
# print(my_list) # [5, 4, 3, 2, 1]

### 3.4.1.10 Lists - collections of data | lists and loops
# # Making use of lists
# my_list = [10, 1, 8, 3, 5]
# total = 0
# for i in range(len(my_list)):
#     total += my_list[i]
# print(total)
# # The second face of the for loop
# my_list = [10, 1, 8, 3, 5]
# total = 0
# for i in my_list:
#     total += i
# print(total)

### 3.4.1.11 Lists - collections of data | lists and loops
# # Lists in action
# # Question: how can you swap the values of two variables?
# variable_1 = 1
# variable_2 = 2
# variable_2 = variable_1
# variable_1 = variable_2 #we lose variable_2

# # we need a third variable that serves as an auxiliary storage:
# variable_1 = 1
# variable_2 = 2
# print(variable_1, variable_2)
#
# auxiliary = variable_1
# variable_1 = variable_2
# variable_2 = auxiliary
# print(variable_1, variable_2)

# # Python offers a more convenient way of doing the swap - take a look:
# variable_1 = 1
# variable_2 = 2
# print(variable_1, variable_2)
#
# variable_1, variable_2 = variable_2, variable_1
# print(variable_1, variable_2)


### 3.4.1.12 Lists - collections of data | lists and loops
# # Lists in action
# # Now you can easily swap the list's elements to reverse their order:
# my_list = [10, 1, 8, 3, 5]
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
# print(my_list) #[5, 3, 8, 1, 10]

# # We can use the for loop to do the same thing automatically,
# # irrespective of the list's length.
# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
# print(my_list) #[5, 3, 8, 1, 10]

### 3.4.1.13 LAB: The basics of lists - the Beatles
# # step 1
# beatles = []
# print("Step 1:", beatles)
# # step 2
# beatles.append('John Lennon')
# beatles.append('Paul McCartney')
# beatles.append('George Harrison')
# print("Step 2:", beatles)
# # step 3
# for i in 'Stu Sutcliffe', 'Pete Best':
#     if 1:#input(f'Add  "{i}"  to the list? Press key <ENTER> if NOT : ') != '':
#         beatles.append(i)
# print("Step 3:", beatles)
# # step 4
# for i in range(2):
#     del beatles[3]
# print("Step 4:", beatles)
# # step 5
# beatles.insert(0, 'Ringo Starr')
# print("Step 5:", beatles)
# # testing list legth
# print("The Fab", len(beatles))

### 3.4.1.14 SECTION SUMMARY
#
# # 1. The list is a type of data in Python used to store multiple objects. It is an ordered and mutable collection of comma-separated items between square brackets, e.g.:
# my_list = [1, None, True, "I am a string", 256, 0]
#
# # 2. Lists can be indexed and updated, e.g.:
# my_list = [1, None, True, 'I am a string', 256, 0]
# print(my_list[3])  # outputs: I am a string
# print(my_list[-1])  # outputs: 0
#
# my_list[1] = '?'
# print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]
#
# my_list.insert(0, "first")
# my_list.append("last")
# print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']
#
# # 3. Lists can be nested, e.g.:
# my_list = [1, 'a', ["list", 64, [0, 1], False]]
# # You will learn more about nesting in module 3.1.7 - for the time being, we just want you to be aware that something like this is possible, too.
#
# # 4. List elements and lists can be deleted, e.g.:
# my_list = [1, 2, 3, 4]
# del my_list[2]
# print(my_list)  # outputs: [1, 2, 4]
#
# del my_list  # deletes the whole list
# # Again, you will learn more about this in module 3.1.6 - don't worry. For the time being just try to experiment with the above code and check how changing it affects the output.
#
# # 5. Lists can be iterated through using the for loop, e.g.:
# my_list = ["white", "purple", "blue", "yellow", "green"]
# for color in my_list:
#     print(color)
#
# # 6. The len() function may be used to check the list's length, e.g.:
# my_list = ["white", "purple", "blue", "yellow", "green"]
# print(len(my_list))  # outputs 5
#
# del my_list[2]
# print(len(my_list))  # outputs 4
#
# # 7. A typical function invocation looks as follows: result = function(arg),
# # while a typical method invocation looks like this:result = data.method(arg).

# # Exercise 1
# # What is the output of the following snippet?
# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 6)
# del lst[0]
# lst.append(1)
# print(lst) # [6, 2, 3, 4, 5, 1]

# # Exercise 2
# # What is the output of the following snippet?
# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0
# for number in lst:
#     add += number
#     lst_2.append(add)
# print(lst_2) # [1, 3, 6, 10, 15]

# # Exercise 3
# # What happens when you run the following snippet?
# lst = []
# del lst
# print(lst) # NameError: name 'lst' is not defined

# # Exercise 4
# # What is the output of the following snippet?
# lst = [1, [2, 3], 4]
# print(lst[1]) # [2, 3]
# print(len(lst)) # 3

### 3.5.1.1 Sorting simple lists - the bubble sort algorithm
# The bubble sort
### 3.5.1.2 Sorting simple lists - the bubble sort algorithm
# # Sorting a list
# my_list = [8, 10, 6, 2, 4]  # list to sort
# for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
#     if my_list[i] > my_list[i + 1]:  # compare adjacent elements
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.

# # You should be able to read and understand this program without any problems:
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list) # [2, 4, 6, 8, 10]

### 3.5.1.3 Sorting simple lists - the bubble sort algorithm
# # The bubble sort - interactive version
# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print("\nSorted:")
# print(my_list)

# ## If you want Python to sort your list, you can do it like this:
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list) # [2, 4, 6, 8, 10]

### 3.5.1.4 SECTION SUMMARY
# # Key takeaways
# # 1. You can use the sort() method to sort elements of a list, e.g.:
# lst = [5, 3, 1, 2, 4]
# print(lst)
# lst.sort()
# print(lst)  # outputs: [1, 2, 3, 4, 5]

# # 2. There is also a list method called reverse(),
# # which you can use to reverse the list, e.g.:
# lst = [5, 3, 1, 2, 4]
# print(lst)
# lst.reverse()
# print(lst)  # outputs: [4, 2, 1, 3, 5]

# # Exercise 1
# # What is the output of the following snippet?
# lst = ["D", "F", "A", "Z"]
# lst.sort()
# print(lst) # ['A', 'D', 'F', 'Z']

# # Exercise 2
# # What is the output of the following snippet?
# a = 3
# b = 1
# c = 2
# lst = [a, c, b]
# lst.sort()
# print(lst) # [1, 2, 3]

# # Exercise 3
# # What is the output of the following snippet?
# a = "A"
# b = "B"
# c = "C"
# d = " "
# lst = [a, b, c, d]
# lst.reverse()
# print(lst) # [' ', 'C', 'B', 'A']

