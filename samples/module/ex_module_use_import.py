""" how to import 'custom' module """
import ex_module_to_import
import ex_module_to_import as mod
from ex_module_to_import import world
from ex_module_to_import import test

# 1st case
print(ex_module_to_import.test('hi'))
ex_module_to_import.world()

# 2nd case
print(mod.test('hi'))
mod.world()

# 3rd case
world()

# 4th case
print(test('hi'))
