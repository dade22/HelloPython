# Boolean values are capitalized
True
False

# negate with not
not True #=> False
not False #=> True

# Equality and Inequality
1 == 1 #=> True
2 == 1 #=> False
1 != 1 #=> False
2 != 1 #=> True

# Comparisons
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True

# Comparisons can be chained!
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

#Logical Operators
3>2 and 2>1 #=> True
2>3 and 2>1 #=> False
2>3 or 2>1 #=> True   

# None is an object (like nil or null)
None #=> None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead
"etc" is None #=> False
None is None  #=> True

"etc" not in "uhuhuhuh" #=> True
"bla" in "yeah bla?" #=> True

# The 'is' operator tests for object identity. This isn't
# very useful when dealing with primitive values, but is
# very useful when dealing with objects.

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
bool(None) #=> False
bool(0)  #=> False
bool("") #=> False