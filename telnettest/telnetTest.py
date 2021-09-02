#!/usr/bin/env python3
import telnetlib

Hosts = ['10.76.153.11', '10.76.153.11', '10.76.153.11']
Ports = ['30100', '30101', '30102']


def do_telnet(Host, Port):
    try:
        tn = telnetlib.Telnet(Host, Port, timeout=5)
        tn.close()
    except:
        return False
    return True


for Host in Hosts:
    for Port in Ports:
        res = do_telnet(Host, Port)
        print(Host + ':' + Port + ' ' + str(res))
