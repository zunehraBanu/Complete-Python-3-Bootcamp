# Constructing a Dictionary

# Make a dictionary with {} and use : to signify a key and a value
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Call values by their key
my_dict['key2']
# Output: 'value2'

# Dictionaries can hold various data types
my_dict = {
    'key1': 123,
    'key2': [12, 23, 33],
    'key3': ['item0', 'item1', 'item2']
}

# Accessing a list stored in the dictionary
my_dict['key3']
# Output: ['item0', 'item1', 'item2']

# Accessing an individual item from that list
my_dict['key3'][0]
# Output: 'item0'

# Calling a string method on that item
my_dict['key3'][0].upper()
# Output: 'ITEM0'

# We can modify values stored in a dictionary
my_dict['key1']
# Output: 123

# Subtract 123 from the value at 'key1'
my_dict['key1'] = my_dict['key1'] - 123
my_dict['key1']
# Output: 0

# Python shorthand for this operation is -=
my_dict['key1'] -= 123
my_dict['key1']
# Output: -123

# We can create keys by assignment
# Start with an empty dictionary
d = {}

# Add keys and values
d['animal'] = 'Dog'
d['answer'] = 42

# Display dictionary
d
# Output: {'animal': 'Dog', 'answer': 42}

# Nesting with Dictionaries

# Dictionary inside a dictionary inside another dictionary
d = {'key1': {'nestkey': {'subnestkey': 'value'}}}

# Accessing the innermost value
d['key1']['nestkey']['subnestkey']
# Output: 'value'

# Dictionary Methods

# Create a sample dictionary
d = {'key1': 1, 'key2': 2, 'key3': 3}

# Return a list-like view of all keys
d.keys()
# Output: dict_keys(['key1', 'key2', 'key3'])

# Return a list-like view of all values
d.values()
# Output: dict_values([1, 2, 3])

# Return a view of all key-value pairs as tuples
d.items()
# Output: dict_items([('key1', 1), ('key2', 2), ('key3', 3)])

# Summary:
# we now know how to:
# - Create dictionaries
# - Retrieve and modify values
# - Nest dictionaries
# - Use basic dictionary methods
