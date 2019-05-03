import time, socket, sys
from threading import Thread


# classe para manipular o socket
class Send:
    def __init__(self):
        self.__msg = ''
        self.new = True
        self.con = None
        self.name = None

    def put(self, msg, name):
        self.__msg = msg
        self.name = name
        if self.con != None:
            # envia um mensagem atravez de uma conexão socket
            self.con.send(self.__msg.encode())
            #print(self.__msg)
            #print(name, ": ", self.__msg)

    def get(self):
        return self.__msg

    def loop(self):
        return self.new


# função esperar - Thread
def esperar(tcp, send, host='localhost', port=5000):
    destino = (host, port)
    # conecta a um servidor
    tcp.connect(destino)

    while send.loop():
        print('Conectado a ', host, '.')
        # atribui a conexão ao manipulador
        send.con = tcp
        while send.loop():
            # aceita uma mensagem
            msg = tcp.recv(1024)
            if not msg: break
            print(str(msg, 'utf-8'))


if __name__ == '__main__':
    print('Digite o nome ou IP do servidor(localhost): ')
    host = input()

    if host == '':
        host = '127.0.0.1'

    # cria um socket
    tcp = socket.socket()
    send = Send()
    # cria um Thread e usa a função esperar com dois argumentos
    processo = Thread(target=esperar, args=(tcp, send, host))
    processo.start()
    print('')

    name = socket.gethostname()
    msg = input()
    while True:
        send.put(msg, name)
        msg = input()

    processo.join()
    tcp.close()
    exit()
