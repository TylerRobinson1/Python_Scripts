import ipaddress
[str(ip) for ip in ipaddress.IPv4Network()]

ip_list = [str(ip) for ip in ipaddress.IPv4Network()]
print(ip_list)

number_of_ip = len(ip_list)
print(number_of_ip)
