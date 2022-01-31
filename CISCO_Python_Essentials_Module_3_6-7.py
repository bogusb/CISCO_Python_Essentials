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


#### Module 3.6 LIST PROCESSING
### 3.6.1.1 Operations on lists
# # The inner life of lists
# Lists (and many other complex Python entities)
# are stored in different ways than ordinary (scalar) variables.
# # You could say that:
#
# - the name of an ordinary variable is the name of its content;
# - the name of a list is the name of a memory location where the list is stored.
# Read these two lines once more - the difference is essential
# for understanding what we are going to talk about next.

# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2) # [2]

### 3.6.1.2 Operations on lists | slices
# # Powerful slices
# # Copying the entire list.
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2) # [1]
#
# # Copying some part of the list.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list) # [8, 6]
#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-3:-1]
# print(new_list) # [6, 4]

### 3.6.1.3 Operations on lists | slices
# # Slices - negative indices
# To repeat:
# - start is the index of the first element included in the slice;
# - end is the index of the first element
#   not included in the slice.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list) # [8, 6, 4]
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-1:1]
# print(new_list) # []

### 3.6.1.4 Operations on lists | slices
# # Slices: continued

# # my_list[:end] equal my_list[0:end]
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:3]
# print(new_list) # [10, 8, 6]

# # my_list[start:] equal my_list[start:len(my_list)]
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[3:]
# print(new_list) # [4, 2]

### 3.6.1.5 Operations on lists | slices, del
# # Slices: continued
# # omitting both start and end
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:]
# print(new_list) # [10, 8, 6, 4, 2]

# # del - can delete slices too:
# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list) # [10, 4, 2]

# # deleting all the elements at once is possible too:
# my_list = [10, 8, 6, 4, 2]
# del my_list[:]
# print(my_list) # []

# # removing the slice from the code changes its meaning dramatically.
# # del instruction will delete the list itself, not its content.
# my_list = [10, 8, 6, 4, 2]
# del my_list
# print(my_list) # NameError: name 'my_list' is not defined

### 3.6.1.6 Operations on lists | in, not in
# # The in and not in operators
# # look through the list in order to check
# # whether a specific value is stored inside the list or not.
# # These operators are:
# # elem in my_list
# # elem not in my_list

# my_list = [0, 3, 12, 8, 2]
# print(5 in my_list) # False
# print(5 not in my_list) # True
# print(12 in my_list) # True

### 3.6.1.7 Lists - more details
# # Lists - some simple programs
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
# print(largest) # 17

# # rewritten - newly introduced form of the for loop:
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# for i in my_list:
#     if i > largest:
#         largest = i
# print(largest)

# # If you need to save computer power, you can use a slice:
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# for i in my_list[1:]:
#     if i > largest:
#         largest = i
# print(largest)

### 3.6.1.8 Lists - more details
# # Lists - some simple programs
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")

# # --------------------------------
# # Let's assume that you've chosen the following numbers
# # in the lottery: 3, 7, 11, 42, 34, 49.
# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0
# for number in bets:
#     if number in drawn:
#         hits += 1
# print(hits) # 4

### 3.6.1.9 LAB: Operating with lists - basics
# # Familiarize the student with:
# # - list indexing;
# # - utilizing the in and not in operators.
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# # Write your code here.
# print("The list with unique elements only:")
# print(my_list)
#
# # # cut from start
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_list = []
#
# while my_list != []:
#     if my_list[0] not in my_list[1:]:
#         new_list.append(my_list[0])
#     del my_list[0]
#
# print("The list with unique elements only:")
# print(new_list)

# # # cut from end
#
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_list = []
#
# while my_list != []:
#     if my_list[-1] not in my_list[:-1]:
#         new_list.append(my_list[-1])
#     del my_list[-1]
#
# print("The list with unique elements only:")
# print(new_list)

### 3.6.1.10 SECTION SUMMARY
# # Key takeaways

# # 1. If you have a list l1, then the following assignment: l2 = l1
# # does not make a copy of the l1 list, but makes the variables l1 and l2
# # point to one and the same list in memory. For example:
#
# vehicles_one = ['car', 'bicycle', 'motor']
# print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']
#
# vehicles_two = vehicles_one
# del vehicles_one[0] # deletes 'car'
# print(vehicles_two) # outputs: ['bicycle', 'motor']

# # 2. If you want to copy a list or part of the list,
# # you can do it by performing slicing:
#
# colors = ['red', 'green', 'orange']
#
# copy_whole_colors = colors[:]  # copy the entire list
# copy_part_colors = colors[0:2]  # copy part of the list

# # 3. You can use negative indices to perform slices, too.
# # For example:
#
# sample_list = ["A", "B", "C", "D", "E"]
# new_list = sample_list[2:-1]
# print(new_list)  # outputs: ['C', 'D']

# # 4. The start and end parameters are optional
# # when performing a slice: list[start:end], e.g.:
#
# my_list = [1, 2, 3, 4, 5]
# slice_one = my_list[2: ]
# slice_two = my_list[ :2]
# slice_three = my_list[-2: ]
#
# print(slice_one)  # outputs: [3, 4, 5]
# print(slice_two)  # outputs: [1, 2]
# print(slice_three)  # outputs: [4, 5]

# # 5. You can delete slices using the del instruction:
#
# my_list = [1, 2, 3, 4, 5]
# del my_list[0:2]
# print(my_list)  # outputs: [3, 4, 5]
#
# del my_list[:]
# print(my_list)  # deletes the list content, outputs: []

# # 6. You can test if some items exist in a list or not
# # using the keywords in and not in, e.g.:
#
# my_list = ["A", "B", 1, 2]
#
# print("A" in my_list)  # outputs: True
# print("C" not in my_list)  # outputs: True
# print(2 not in my_list)  # outputs: False

# # # Exercise 1
# # # What is the output of the following snippet?
# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
# del list_1[0]
# del list_2[0]
# print(list_3) # ['C']

# # # Exercise 2
# # # What is the output of the following snippet?
# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
# del list_1[0]
# del list_2
# print(list_3) # ['B', 'C']

# # # Exercise 3
# # # What is the output of the following snippet?
# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
# del list_1[0]
# del list_2[:]
# print(list_3) # []

# # # Exercise 4
# # # What is the output of the following snippet?
# list_1 = ["A", "B", "C"]
# list_2 = list_1[:]
# list_3 = list_2[:]
# del list_1[0]
# del list_2[0]
# print(list_3) # ['A', 'B', 'C']

# # # Exercise 5
# # # Insert in or not in instead of ???
# # # so that the code outputs the expected result.
# # my_list = [1, 2, "in", True, "ABC"]
# # print(1 ??? my_list)  # outputs True
# # print("A" ??? my_list)  # outputs True
# # print(3 ??? my_list)  # outputs True
# # print(False ??? my_list)  # outputs False
#
# my_list = [1, 2, "in", True, "ABC"]
# print(1 in my_list)  # outputs True
# print("A" not in my_list)  # outputs True
# print(3 not in my_list)  # outputs True
# print(False in my_list)  # outputs False

### 3.7.1 Multidimensional arrays
### 3.7.1.1 Lists in advanced applications

# # # Lists in lists
# WHITE_PAWN = 'O'
# # row = []
# # for i in range(8):
# #    row.append(WHITE_PAWN)
# row = [WHITE_PAWN for i in range(8)]
# print(row)

# # # Let us show you some other list comprehension examples:
# # # Example #1:
# squares = [x ** 2 for x in range(10)]
# # The snippet produces a ten-element list filled with squares
# # of ten integer numbers starting from zero
# # (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
#
# # # Example #2:
# twos = [2 ** i for i in range(8)]
# # The snippet creates an eight-element array
# # containing the first eight powers of two
# # (1, 2, 4, 8, 16, 32, 64, 128)
#
# # # Example #3:
# odds = [x for x in squares if x % 2 != 0 ]
# # The snippet makes a list with only the odd elements
# # of the squares list.
#
# print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(twos) # [1, 2, 4, 8, 16, 32, 64, 128]
# print(odds) # [1, 9, 25, 49, 81]

### 3.7.1.2 Lists in advanced applications | Arrays
# # # Lists in lists: two-dimensional arrays
# # # Let's also assume that a predefined symbol named EMPTY
# # # designates an empty field on the chessboard.
#
# EMPTY = '.'
# # board = []
# # for i in range(8):
# #     row = [EMPTY for i in range(8)]
# #     board.append(row)
# board = [[EMPTY for i in range(8)] for j in range(8)]
# print(board)

### 3.7.1.3 Lists in advanced applications | Arrays
# # Lists in lists: two-dimensional arrays - continued

# EMPTY = '....'
# KNIGHT = 'KNIGHT'
# PAWN = 'PAWN'
# ROOK = 'ROOK'
# board = []
#
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
#
# # add all the rooks
# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
# # add a knight to C4
# board[4][2] = KNIGHT
# # add a pawn to E5
# board[3][4] = PAWN
#
# print(board)

### 3.7.1.4 Lists in advanced applications | Arrays
# # Multidimensional nature of lists: advanced applications
# Let's go deeper into the multidimensional nature of lists.
# To find any element of a two-dimensional list, you have to use two coordinates:
# a vertical one (row number)
# and a horizontal one (column number).

# # Now it's time to determine the monthly average noon temperature.
# # Add up all 31 readings recorded at noon and divide the sum by 31.
# # You can assume that the midnight temperature is stored first.
# # Here's the relevant code:
#
# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # The matrix is magically updated here.
# #
# total = 0.0
#
# for day in temps:
#     total += day[11]
#
# average = total / 31
#
# print("Average temperature at noon:", average)

# # Now find the highest temperature during
# # the whole month - see the code:
# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # The matrix is magically updated here.
# #
#
# highest = -100.0
#
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
#
# print("The highest temperature was:", highest)

# # Now count the days when the temperature at noon
# # was at least 20 ℃:
#
# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # The matrix is magically updated here.
# #
#
# hot_days = 0
#
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
#
# print(hot_days, "days were hot.")

### 3.7.1.5 Lists in advanced applications | Arrays
# # Three-dimensional arrays
# # Python does not limit the depth of list-in-list inclusion.
# # Here you can see an example of a three-dimensional array:
# # Imagine a hotel:
# # First step - the type of the array's elements.
# # In this case, a Boolean value (True/False) would fit.
# # Step two - calm analysis of the situation.
# # Summarize the available information: three buildings, 15 floors, 20 rooms.
# # Now you can create the array:
#
# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#
# # The first index (0 through 2) selects one of the buildings;
# # the second (0 through 14) selects the floor,
# # the third (0 through 19) selects the room number. All rooms are initially free.
# # Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:
# rooms[1][9][13] = True
# # and release the second room on the fifth floor located in the first building:
# rooms[0][4][1] = False
# # Check if there are any vacancies on the 15th floor of the third building:
#
# vacancy = 0
#
# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1
#
# # The vacancy variable contains 0 if all the rooms are occupied,
# # or the number of available rooms otherwise.

### 3.7.1.6 SECTION SUMMARY
# # Key takeaways
# # 1. List comprehension allows you to create new lists from existing ones in a concise and elegant way.
# # The syntax of a list comprehension looks as follows:
#
# [expression for element in list if conditional]
#
# # which is actually an equivalent of the following code:
#
# for element in list:
#     if conditional:
#         expression
#
# # Here's an example of a list comprehension - the code creates a five-element list
# # filled with with the first five natural numbers raised to the power of 3:
#
# cubed = [num ** 3 for num in range(5)]
# print(cubed)  # outputs: [0, 1, 8, 27, 64]

# # 2. You can use nested lists in Python to create matrices
# # (i.e., two-dimensional lists). For example:
# # A four-column/four-row table - a two dimensional array (4x4)
#
# table = [[":(", ":)", ":(", ":)"],
#          [":)", ":(", ":)", ":)"],
#          [":(", ":)", ":)", ":("],
#          [":)", ":)", ":)", ":("]]
#
# print(table)
# print(table[0][0])  # outputs: ':('
# print(table[0][3])  # outputs: ':)'

# # 3. You can nest as many lists in lists as you want,
# # and therefore create n-dimensional lists, e.g., three-, four-
# # or even sixty-four-dimensional arrays. For example:
# # Cube - a three-dimensional array (3x3x3)
#
# cube = [[[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':(', 'x', 'x']],
#
#         [[':)', 'x', 'x'],
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],
#
#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]
#
# print(cube)
# print(cube[0][0][0])  # outputs: ':('
# print(cube[2][2][0])  # outputs: ':)'

### 3.7.1.7 Module Completion
# # Here's a short summary of the objectives you've covered
# # and got familiar with in Module 3:
# # - Boolean values to compare different values and control the execution paths
# #   using the if and if-else instructions;
# # - the utilization of loops (while and for) and how to control their behavior
# #   using the break and continue instructions;
# # - the difference between logical and bitwise operations;
# # - the concept of lists and list processing, including the iteration
# #   provided by the for loop, and slicing;
# # - the idea of multi-dimensional arrays.

# for i in range(1):
#     print('#')
# else:
#     print('#')

# var = 1
# while var < 10:
#     print('#')
#     var = var << 1
