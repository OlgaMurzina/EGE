from ipaddress import *

ip_net = ip_interface('146.180.173.153/255.192.0.0').network
for x in ip_net.hosts():
    pass
print(x, sum([int(y) for y in str(x).split('.')]))
print(list(ip_net)[-2])
