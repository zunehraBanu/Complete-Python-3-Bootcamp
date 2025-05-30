# Constructing Tuples

# Tuples are created using parentheses () and commas between elements
t = (1, 2, 3)

# You can check the length of a tuple just like a list
len(t)
# Output: 3

# Tuples can hold mixed data types
t = ('one', 2)

# Display the tuple
t
# Output: ('one', 2)

# Access elements using indexing (same as lists)
t[0]
# Output: 'one'

# Slicing also works like lists
t[-1]
# Output: 2

# Basic Tuple Methods

# .index() returns the first index of a specified value
t.index('one')
# Output: 0

# .count() returns how many times a value appears
t.count('one')
# Output: 1

# Immutability

# Tuples are immutable — they cannot be changed after creation
# Trying to change a value will raise a TypeError
t[0] = 'change'
# TypeError: 'tuple' object does not support item assignment

# Tuples also don’t support list-like methods such as .append()
t.append('nope')
# AttributeError: 'tuple' object has no attribute 'append'

# When to Use Tuples

# Tuples are useful when you want to ensure data cannot be changed
# For example: fixed configurations, coordinates, or safe keys for dictionaries

# Summary:
# - Tuples are like immutable lists
# - Use them when you need to protect data from being changed
# - You can index, slice, and use basic methods like count() and index()
