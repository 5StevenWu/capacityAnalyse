#!/usr/bin/env python3
import telnetlib
import time
#yum install python3 (centos7.9)
#要请求的IP和端口号
Host = '192.168.89.135'
Port = '22'

def do_telnet(Host, Port):
    try:
        tn = telnetlib.Telnet(Host, Port, timeout=5)
        tn.close()
    except:
        return False
    return True

while True:
    time.sleep(5)
    res = do_telnet(Host, Port)
    print(str(Host) + ':' + str(Port) + ' ' + str(res))
