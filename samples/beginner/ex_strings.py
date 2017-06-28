# Strings are created with single or double-quotes
A = "This is a string."
print(A)

A = 'This is also a string.'
print(A)

# Strings can be added too!
A = "Hello " + "world!" #=> "Hello world!"
print(A)

# A string can be treated like a list of characters
A = "This is a string"[0] #=> 'T'
print(A)

# % can be used to format strings:
A = "%s can be %s" % ("strings", "interpolated")
#=> 'strings can be interpolated'
print(A)

# A newer, preferred way to format strings is the format method.
A = "{0} can be {1}".format("strings", "formatted")
#=> 'strings can be formatted'
print(A)

# You can use keywords if you don't want to count.
A = "{name} wants to eat {food}".format(name="Bob", food="lasagna")
#=> 'Bob wants to eat lasagna'
print(A)

if "blah" not in "uh nothing to say?": 
    print("not found blah")
else: print("found blah")

if "blah" in "blah? sure": 
    print("found blah")
else: print("not found blah")

