import socket
import time

# Enable broadcasting mode
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.2)

while True:
    server.sendto(b"your very important message", ('239.255.255.250', 1980))
    print("message sent!")
    time.sleep(1)