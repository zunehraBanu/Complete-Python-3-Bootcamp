# Formatting with placeholders
# You can use %s to inject strings into your print statements.
# The modulo % is referred to as a "string formatting operator".

print("I'm going to inject %s here." %'something')
# I'm going to inject something here.

# You can pass multiple items by placing them inside a tuple after the % operator.
print("I'm going to inject %s text here, and %s text here." %('some','more'))
# I'm going to inject some text here, and more text here.

# You can also pass variable names:
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))
# I'm going to inject some text here, and more text here.

# Format conversion methods.
# %s and %r convert any python object to a string using str() and repr()
print('He said his name was %s.' %'Fred')
print('He said his name was %r.' %'Fred')
# He said his name was Fred.
# He said his name was 'Fred'.

# As another example, \t inserts a tab into a string.
print('I once caught a fish %s.' %'this \tbig')
print('I once caught a fish %r.' %'this \tbig')
# I once caught a fish this 	big.
# I once caught a fish 'this \tbig'.

# %s converts everything to string; %d converts to integer
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)
# I wrote 3.75 programs today.
# I wrote 3 programs today.

# Padding and Precision of Floating Point Numbers
print('Floating point numbers: %5.2f' %(13.144))
print('Floating point numbers: %1.0f' %(13.144))
print('Floating point numbers: %1.5f' %(13.144))
print('Floating point numbers: %10.2f' %(13.144))
print('Floating point numbers: %25.2f' %(13.144))
# Floating point numbers: 13.14
# Floating point numbers: 13
# Floating point numbers: 13.14400
# Floating point numbers:      13.14
# Floating point numbers:                     13.14

# Multiple Formatting
print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))
# First: hi!, Second:  3.14, Third: 'bye!'

# Formatting with the .format() method
# A better way to format objects into your strings for print statements
print('This is a string with an {}'.format('insert'))
# This is a string with an insert

# 1. Inserted objects can be called by index position:
print('The {2} {1} {0}'.format('fox','brown','quick'))
# The quick brown fox

# 2. Inserted objects can be assigned keywords:
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
# First Object: 1, Second Object: Two, Third Object: 12.3

# 3. Inserted objects can be reused, avoiding duplication:
print('A %s saved is a %s earned.' %('penny','penny'))
# A penny saved is a penny earned.
print('A {p} saved is a {p} earned.'.format(p='penny'))
# A penny saved is a penny earned.

# Alignment, padding and precision with .format()
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
# Fruit    | Quantity 
# Apples   |       3.0
# Oranges  |        10

# Left, center, and right alignment
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
# Left     |  Center  |    Right
# 11       |    22    |       33

# Padding character with alignment
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
# Left==== | -Center- | ...Right
# 11====== | ---22--- | ......33

# Float formatting: placeholders vs format method
print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))
# This is my ten-character, two-decimal number:     13.58
# This is my ten-character, two-decimal number:     13.58

# Formatted String Literals (f-strings)
# Introduced in Python 3.6
name = 'Fred'
print(f"He said his name is {name}.")
# He said his name is Fred.

# Pass !r to get the string representation
print(f"He said his name is {name!r}")
# He said his name is 'Fred'

# Float formatting with f-strings
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
# My 10 character, four decimal number is:   23.4568
# My 10 character, four decimal number is:   23.4568

# Padding behavior difference
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
# My 10 character, four decimal number is:   23.4500
# My 10 character, four decimal number is:     23.45

# You can use format() inside f-strings to preserve padding
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")
# My 10 character, four decimal number is:   23.4500
# My 10 character, four decimal number is:   23.4500
