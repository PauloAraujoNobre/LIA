import time, socket, sys

print('Sendo Server...')
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Nome: ')
soc.listen(1)
print('Esperando corno se conetar...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "\n")
print('Conecção Estabelecida. IP: {}'.format(addr[0]))
client_name = connection.recv(1024)
client_name = client_name.decode()
print('{} entrou.'.format(client_name))
print('Escreva "flws" pra sair.')
connection.send(name.encode())
while True:
   message = input('Eu > ')
   if message == 'flws':
      message = 'Fui di base'
      connection.send(message.encode())
      print("\n")
      break
   connection.send(message.encode())
   message = connection.recv(1024)
   message = message.decode()
   print(client_name, '>', message)
   if message == "Fui di base":
      print("O corno saiu, vc deve sair tbm.")
      break
