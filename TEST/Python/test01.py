#!/usr/bin/env python3

import time
import nmap

def formatSub(target):
    target = target.split(".")
    a = "."
    target = target[0] + a + target[1] + a + target[2]+ a + "0/24"
    return target

host = formatSub("192.168.1.200")
scanner = nmap.PortScanner()

def subnetDiscoveryNmap():
    print("SubNetScan Started")
    t1 = time.time()
    scanner.scan(hosts=host, arguments="-T5 -sn")
    t2 = time.time() - t1
    print("scan terminated in : ", t2)

def get_output():
    scaninfo = scanner.scaninfo()
    print("scaninfo :", scaninfo)

    all_host = scanner.all_hosts()
    print("all_hosts : ", all_host)

# 3.64 s
# 4.45 s
# 3.57 s
# 4.55 s
# 5.14 s

subnetDiscoveryNmap()
get_output()
