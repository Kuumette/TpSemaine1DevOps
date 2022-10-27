import ipaddress

# IP = '192.168.32.16'
# MASK = '255.255.0.0'
print("Merci de rentrer une adresse IP")
IP = input()
print("Vous avez rentrer: ", IP)
print("maintenant un mask de sous reseau")
MASK = input()
print("vous avez choisi: ", MASK )



def ip():
    host = ipaddress.IPv4Address(IP)
    return host

def mask():
    net = ipaddress.IPv4Network(IP + '/' + MASK, False)
    return net

def subnet():
    print('Subnet:', ipaddress.IPv4Address(int(ip()) & int(mask().netmask)))

def host():
    print('Host:', ipaddress.IPv4Address(int(ip()) & int(mask().hostmask)))

def broadcast():
    print('Broadcast:', mask().broadcast_address)

def main():
    subnet()
    host()
    broadcast()

if __name__ == '__main__':
    main()