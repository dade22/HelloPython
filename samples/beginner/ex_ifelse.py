# if can be used as an expression
# Equivalent of C's '?:' ternary operator

print("Yahoo!" if 3 > 2 else "Google!")  # => "Yahoo!"
print("Yahoo!" if 1 > 2 else "Google!")  # => "Google!"

# like these 

if 1 > 2: print("Google!")
else: print("Yahoo!")

if 3 > 2: print("Google!")
else: print("Yahoo!")