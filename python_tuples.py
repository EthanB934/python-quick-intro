# Tuples are immutable lists, the items within cannot be changed.
# Tuples are created using () instead []

# Tuple defined as rgb, initialized with strings

rgb = ("Red", "Green", "Blue")

# Tuples may be indexed

print(rgb[0])
print(rgb[1])
print(rgb[2])

# Tuples do not allow for reassignment rgb[0] = 'yellow'

# If a tuple should only contain one item, it must be trailed by a comma

numbers = (1,)
print(numbers[0])

# Type funciton returns data type after evaluation

print(type(numbers))
print(type(numbers[0]))

# Tuple variable can be reassigned tuples

colors = ("Blue", "Orange", "Pink")
print(colors)
colors = ("Black", "Grey", "Brown")
print(colors)
