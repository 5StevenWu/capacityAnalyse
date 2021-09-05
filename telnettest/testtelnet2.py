#!/usr/bin/env python2
import telnetlib

import time

# yum install python3 (centos7.9)
Host = '192.168.89.137'
Port = '22'


def do_telnet(Host, Port):
    try:
        tn = telnetlib.Telnet(Host, Port, timeout=5)
        tn.close()
    except:
        return False
    return True


while True:

    res = do_telnet(Host, Port)
    print(str(Host) + ':' + str(Port) + ' ' + str(res))
    time.sleep(5)