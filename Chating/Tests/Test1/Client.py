import time, socket, sys
print('Servidor do Cliente...')
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, '({})'.format(ip))
server_host = input('Digite o IP do server:')
name = input('Nome do cliente: ')
port = 1234
print('Tentando conectar no serverr: {}, ({})'.format(server_host, port))
soc.connect((server_host, port))
print("Conectado...\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} entrou.'.format(server_name))
print('Escreva "flws" pra sair.')
while True:
    message = soc.recv(1024)
    message = message.decode()
    print(server_name, ">", message)
    if message == "Fui di base":
        print("O corno saiu, vc deve sair tbm.")
        break
    message = input(str("Eu > "))
    if message == "flws":
        message = "Fui di base"
        soc.send(message.encode())
        print("\n")
        break
    soc.send(message.encode())
