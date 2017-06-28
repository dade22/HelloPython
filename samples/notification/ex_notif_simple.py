#!/usr/bin/python
# -*- coding: utf-8 -*-

import notify2
import time
import os

os.system("samples/run_as_script/ex_script_recalled.py")

notify2.init("Test", None)
n = notify2.Notification("Summary")
n.show()

time.sleep(2)

n.update("Summary3", "Message3")
n.show()

time.sleep(2)

