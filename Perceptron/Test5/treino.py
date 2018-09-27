import numpy as np

class Treino():

    def __init__(self, pesos, taxaDeAprend, target, tamCol, tamRow, amostras, epocas):
        self.pesos = pesos
        self.taxaDeAprend = taxaDeAprend
        self.target = target
        self.tamCol = tamCol
        self.tamRow = tamRow
        self.amostras = amostras
        self.epocas = epocas

    def ativacao(self, u):
        if (np.sum(u) >= 0):
            return  1
        else:
            return  -1

    def treinar(self):

        for i in range(self.tamRow):
            erro = 1
            while erro == 1:
                u = np.multiply(self.amostras[i], self.pesos)

                self.output =  self.ativacao(u)

                if(self.target[i] != self.output):
                    e = self.target[i] - self.output
                    aux = e * self.taxaDeAprend
                    variacao = np.multiply(aux, self.amostras[i])
                    self.pesos = np.add(variacao, self.pesos)
                else:
                    erro = 0
                self.epocas += 1
        return (self.pesos, self.epocas)

    def testar(self,testes):


        #testes = np.genfromtxt('testes.csv', delimiter=',')
        testes = testes.copy()
        target = testes[: , 0].copy()
        testes[:, 0] = 1

        acertos = 0
        [tamColuna  , tamLinha] = testes.shape
        total = tamColuna

        for x in range(tamColuna):
            soma = np.multiply(testes[x], self.pesos)
            predicted = self.ativacao(soma)
            if predicted == target[x]:
                acertos += 1


        print("A taxa de acertos desse algoritmo {}".format(acertos/total * 100 ))
