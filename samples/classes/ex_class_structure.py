""" student class used like a simple structure, without logics """
class Student:
     def __init__ (self, name, age, gender):
         self.name   = name
         self.age    = age
         self.gender = gender
 
Sue = Student("Susan Miller", 20, "f")
print(Sue) # <__main__.Student instance at 0x.....>
print(Sue.age) # 20
print(Sue.gender) # f
