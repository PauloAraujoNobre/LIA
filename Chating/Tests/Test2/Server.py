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
def esperar(tcp, send, host='', port=5000):
    origem = (host, port)
    # cria um vinculo
    tcp.bind(origem)
    # deixa em espera
    tcp.listen(1)

    while True:
        # aceita um conexão
        con, cliente = tcp.accept()
        print('Cliente ', cliente, ' conectado!')
        # atribui a conexão ao manipulador
        send.con = con

        while True:
            # aceita uma mensagem
            msg = con.recv(1024)
            if not msg: break
            print(str(msg, 'utf-8'))


if __name__ == '__main__':
    # cria um socket
    tcp = socket.socket()
    send = Send()
    # cria um Thread e usa a função esperar com dois argumentos
    processo = Thread(target=esperar, args=(tcp, send))
    processo.start()

    print('Iniciando o servidor de chat!')
    print('Aguarde alguém conectar!')

    name = socket.gethostname()
    msg = input()
    while True:
        send.put(msg, name)
        msg = input()

    processo.join()
    tcp.close()
    exit()
