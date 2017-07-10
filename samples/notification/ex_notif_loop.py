""" Useful script to check if VPN is on """
#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
import notify2

ptimecon = 1 # polling time (sec) when connected
ptimedis = 10 # polling time (sec) when disconnected
debug = False # print something
vpnip = ["91.121.103.225", "195.154.128.163"] # valid vpn ip (1+)

def underVpn():

    for ip in vpnip:

        command = "ip r | grep " + ip
        if debug: print(command)

        output = os.popen(command).read()
        if debug: print("%s contained in %s ?" % (vpnip, output))

        if ip in output:
            return True
    return False

# Let's go..

notify2.init("ex_notif", None)
n = notify2.Notification("", "")

broken = False

while True:

    if underVpn():

        if broken:

            n.icon = "security-high"
            n.update("ok", "connection is back")
            n.show()
            time.sleep(ptimecon)

        broken = False
        n.close()
        continue

    broken = True
    n.icon = "security-low"
    n.update("ehi", "check connection before continue")
    n.show()

    time.sleep(ptimedis)
