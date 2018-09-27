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

    def treinar(self):

        for i in range(self.tamRow):
            erro = 1
            while erro == 1:
                test = np.multiply(self.amostras[i], self.pesos)
                if(np.sum(test) > 0):
                    self.output = 1
                else:
                    self.output = -1
                if(self.target[i] != self.output):
                    e = self.target[i] - self.output
                    print("\n\n\n")
                    variacao = np.multiply(e * self.taxaDeAprend, self.amostras[i])
                    print(".")
                    print(self.pesos)
                    print("\n\n\n")
                    print(variacao)

                    self.pesos += variacao
                    #print(variacao)
                else:
                    erro = 0
                self.epocas += 1
        return (self.pesos, self.epocas)
