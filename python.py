import socket
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp.bind(("0.0.0.0", 8000))
tcp.listen(3)
print ("wating for client")

(client, (ip, port)) = tcp.accept()

print ("client ip is " +ip)

print ("staring to echo")
data = "yes got you "

while len(data):
    data = client.recv(2048).decode('utf-8')

    print ("client send :", data)
    client.send(str.encode(data))

print ("closing connection ")
client.close()
