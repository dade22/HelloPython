#!/usr/bin/env python3.5
""" HowTo: Richiamare uno script da uno script """
import os

# anche se non usato la dichiarazione di 
#      import ex_script_recalled
#
# fa "scattare" proprio l'esecuzione dello
# script ex_script_recalled.py

import ex_script_recalled


print("__package__: %s" % __package__)
print("__file__: %s" % __file__)
print("__name__: %s" % __name__)
print("os.curdir: %s" % os.curdir)

# metodo per richiamare uno script da linea di comando,
# come se fosse eseguito tramite shell
os.system("samples/run_as_script/ex_script_recalled.py")
