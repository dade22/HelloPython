""" HowTO use a simple class """

class Basket:
    """ Simple Basket class """

    # Ricorda sempre l'argomento *self*
    def __init__(self, contents=None):
        """ constructor """
        self.contents = contents or []

    def add(self, element):
        """ simple method """
        self.contents.append(element)

    def print_me(self):
        """ explicit print method """
        print("Contiene: %s" % self)

    def __str__(self):
        """ when a conversion in str is recalled """
        result = ""
        for element in self.contents:
            result = result + " " + element
        return result.strip()


# HOW TO
# simple recall of Basket
b = Basket(['apple', 'orange'])
b.add("lemon")
b.print_me()

# print b
print(b)
