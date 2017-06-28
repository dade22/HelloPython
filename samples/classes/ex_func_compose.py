from math import sin, cos

y = 3

# Nota che qui stiamo usando funzioni come argomento... 
# il che è un trucco già parecchio carino in sè.

def compose1(fun1, fun2):

    def inner(x, fun1=fun1, fun2=fun2):
        return fun1(fun2(x))
    return inner

sincos = compose1(sin, cos)
x = sincos(y)
print("x=%s" % x, "y=%s" % y)

# altro modo di scrivere compose è il seguente che risulta
# molto più conciso e anonima

def compose2(f1, f2):

    # vedere "ex_functions.py" per maggiori informazioni / esempi
    return lambda x, f1=f1, f2=f2: f1(f2(x))

sincos = compose1(sin, cos)
x = sincos(y)
print("x=%s" % x, "y=%s" % y)



