'''
Для узла с IP-адресом 111.81.93.127 адрес сети равен 111.81.80.0. Чему равен третий слева байт маски?
Ответ запишите в виде десятичного числа.
'''

from ipaddress import*

ip_ad = ip_address('111.81.93.127')  # для проверки, что найдена нужная сеть

for mask in range(20, 33):
    ip_net = ip_interface(f'111.81.80.0/{mask}').network
    if ip_ad in ip_net:
        print(ip_net.netmask, mask)
print(bin(80)[2:].rjust(8, '0'))
print(bin(93)[2:].rjust(8, '0'))
