""" HowTo: importare un modulo """

import datetime # 1° modo
from datetime import date # 2° modo

# Usando il 1° modo ..
x = datetime.date(2017, 1 , 31)
print("x=%s" % x)

# Oppure...

# Usando il 2° modo ..
x = date(2017, 1 , 31)
print("x=%s" % x)