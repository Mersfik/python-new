import socket

target_host = "www.bancocn.com"
target_port = 80

#criando um objeto socket:
client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

#conectar ao cliente:
client.connect ((target_host, target_port))

#enviar dados ao cliente:
client.send(b"GET / HTTP/ 1.1\r\nHost: bancocn.com\r\n\r\n")

#receber dados do cliente:
response = client.recv(4096)
print(response.decode())
client.close()
    
