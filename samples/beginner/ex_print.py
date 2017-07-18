#!/usr/bin/python3

"""
print examples
"""

# simplest
print("Hello World")

# print a number
C = 50
F = C * 9 / 5 + 32
print(F)

# print formatted string
A = 100
A /= 10
print("1st method // a=%s" % A)
print("2nd method // a=" + str(A))

# print conditionated
x = 3
if x > 0:
    print("x is positive")
else:
    print("x is zero or negative")

# array
name = ["Cleese", "John"]
print(name[1], name[0]) # Stampa "John Cleese"

x = ["spam", "spam", "spam", "spam", "spam", "eggs", "and", "spam"]
print(x[5:7]) # Stampa la lista ["eggs","and"]

# function
def square(X):
    """
    square method
    """
    return X*X

print("square(2): %s" % square(2)) # Result is 4

# simple function alias
queeble = square
print("queeble(2): %s" % queeble(2)) # Always 4

# mutiple variables: simple format - new style
dollars = 23
cents = 34
print("He has ${0}.{1}".format(dollars, cents))

# mutiple variables: all styles
name = "John"
score = 99.3

print("-- old style --")
print("1: Total score for %s is %s" % (name, score))
print("-- new style --")
print("1: Total score for {} is {}".format(name, score))
print("2: Total score for {0} is {1}".format(name, score))
print("3: Total score for {1} is {0}".format(score, name))

# print multiple time a char
print('-' * 22) 
