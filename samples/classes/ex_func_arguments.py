""" ex classes """
def orange_juice():
    return x*2

x = 3
y = orange_juice()
print("x=%s" % x, "y=%s" % y) # y è ora 6

x = 1
y = orange_juice()
print("x=%s" % x, "y=%s" % y) # y è ora 2

# different is something like this..

x = 4
def apple_juice(x=x):
    return x*2

# l'argomento x riceve un valore di default che è eguale al valore della
# variabile x nel momento in cui la funzione viene definita. Quindi,
# sinchè nessuno fornisce un argomento per la funzione, si comporterà così:

x = 3
y = apple_juice()
print("x=%s" % x, "y=%s" % y) # y is now 8

x = 1
y = apple_juice()
print("x=%s" % x, "y=%s" % y) # y is now 8

x = 7
y = apple_juice(1)
print("x=%s" % x, "y=%s" % y) # y is now 2 // not 8




