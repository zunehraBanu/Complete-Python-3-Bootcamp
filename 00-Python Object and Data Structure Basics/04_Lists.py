# Lists are constructed with brackets [] and commas separating every element in the list.

# Assign a list to a variable named my_list
my_list = [1, 2, 3]

# We just created a list of integers, but lists can actually hold different object types.
my_list = ['A string', 23, 100.232, 'o']

# Just like strings, the len() function will tell you how many items are in the sequence of the list.
len(my_list)
# 4

# Indexing and Slicing
# Indexing and slicing work just like in strings.

my_list = ['one', 'two', 'three', 4, 5]

# Grab element at index 0
my_list[0]
# 'one'

# Grab index 1 and everything past it
my_list[1:]
# ['two', 'three', 4, 5]

# Grab everything UP TO index 3
my_list[:3]
# ['one', 'two', 'three']

# We can also use + to concatenate lists, just like we did for strings.
my_list + ['new item']
# ['one', 'two', 'three', 4, 5, 'new item']

# Note: This doesn't actually change the original list!
my_list
# ['one', 'two', 'three', 4, 5]

# You would have to reassign the list to make the change permanent.
# Reassign
my_list = my_list + ['add new item permanently']
my_list
# ['one', 'two', 'three', 4, 5, 'add new item permanently']

# We can also use the * for a duplication method similar to strings:
# Make the list double
my_list * 2
# ['one', 'two', 'three', 4, 5, 'add new item permanently', 'one', 'two', 'three', 4, 5, 'add new item permanently']

# Again, doubling is not permanent
my_list
# ['one', 'two', 'three', 4, 5, 'add new item permanently']

# Basic List Methods
# Lists in Python have no fixed size or type constraint.

# Create a new list
list1 = [1, 2, 3]

# Use the append method to permanently add an item to the end of a list:
list1.append('append me!')
# Show
list1
# [1, 2, 3, 'append me!']

# Use pop to "pop off" an item from the list.
# Pop off the 0 indexed item
list1.pop(0)
# 1

# Show remaining list
list1
# [2, 3, 'append me!']

# Assign the popped element (default popped index is -1)
popped_item = list1.pop()
popped_item
# 'append me!'

# Show remaining list
list1
# [2, 3]

# It should also be noted that list indexing will return an error if there is no element at that index.
# Example: list1[100] will throw IndexError
# list1[100]  # Uncommenting this will raise IndexError: list index out of range

# We can use the sort method and the reverse method to also affect your lists:

new_list = ['a', 'e', 'x', 'b', 'c']

# Show
new_list
# ['a', 'e', 'x', 'b', 'c']

# Use reverse to reverse order (this is permanent!)
new_list.reverse()
new_list
# ['c', 'b', 'x', 'e', 'a']

# Use sort to sort the list (alphabetical order or ascending for numbers)
new_list.sort()
new_list
# ['a', 'b', 'c', 'e', 'x']

# Nesting Lists
# Python data structures support nesting. For example, a list inside a list.

# Let's make three lists
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

# Make a list of lists to form a matrix
matrix = [lst_1, lst_2, lst_3]

# Show
matrix
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Grab first item in matrix object
matrix[0]
# [1, 2, 3]

# Grab first item of the first item in the matrix object
matrix[0][0]
# 1

# List Comprehensions
# Python has an advanced feature called list comprehensions.

# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
first_col
# [1, 4, 7]

# We used a list comprehension here to grab the first element of every row in the matrix object.

# For more advanced methods and features of lists in Python,
# check out the Advanced Lists section later on in this course!
