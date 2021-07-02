# This small code listens to the broadcast. See also SSDP advertisement
# This is how IoT devices find each other 

import socket
import struct
 
MCAST_GRP = '239.255.255.250'
localIP     = "0.0.0.0"
localPort   = 1980
bufferSize  = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY))
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    print("Message from Client:{}".format(message))
    print("Client IP Address:{}".format(address))