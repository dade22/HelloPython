""" Funzioni lambda (anonime) """

# Python supporta funzioni anonime semplici attraverso la forma lambda.
# Il corpo d'esecuzione della lambda deve essere una espressione e non 
# una dichiarazione, e quindi questa è una restrizione alla sua utilità.
# Il valore ritornato dalla lambda è il valore contenuto nell'espressione.

foo = lambda x: x*x
print(foo(10))

# equivale a qualcosa tipo

def foo1(x):
    return x*x
print(foo1(10))


# Altri esempi di utilizzo delle lambda ..


# Es1 - An input list: apply lambda to all elements with map.
items = [1, 2, 3]
for r in map(lambda x: x + 1, items):
    print(r)


# Es2 - Sum result of map
names = ["Turin", "San Jose", "San Francisco", "Santa Fe", "Houston"]
count = sum(map(lambda s: s.startswith("San"), names))
print("{} di {} iniziano con San".format(count, len(names)))

