import numpy as np


class RedeNeural():

    def __init__(self, amostras, target):
        self.amostras = amostras
        self.target = target
        self.epoch = 0
        [self.row, self.col] = self.amostras.shape
        self.learning_rate = np.random.rand(1, 1)
        #self.weights1 = np.random.rand(3, 2)
        self.weights1 = np.matrix([[1, 1], [2, 2], [3, 3]])
        #self.weights2 = np.random.rand(2, 3)
        self.weights2 = np.matrix([[1, 1, 1], [2, 2, 2]])
        self.bias = np.random.rand(1)
        self.targetDegrau = [0, 1]
        #print(self.bias)
        #print(self.weights1)
        #print("\n")
        #print(self.weights2)

    def train(self):
        self.count = 0
        while (self.epoch < 100 or self.delta_erro < 0.01):
            self.shuffle()
            self.zera_count()
            for i in range(self.row):
                self.output = self.predict(i)
                print(self.output)
                print("\n\n")
                vetor_um_zero = self.vetor_um_zero(self.output)
                print(self.output)
                print("\n\n")

                for k in range(len(self.output)):
                    if vetor_um_zero[k] != self.targetDegrau[k]:
                        erro = 1
                        self.cria_erro(np.max(self.output))
                    else:
                        self.cria_erro(np.max(self.output))

            if erro == 1:
                self.train_weights()
            self.epoch += 1
        return (self.weights, self.epoch)

    def predict(self, i):
        linha = self.amostras[i, :]
        linha = linha[:, :-1]
        #print(linha)            #a = [x1, x2]
        #print(self.weights1)    #w = [[w11, w21][w12, 22][w13, w23]]
        y = np.multiply(linha, self.weights1)
        y = np.sum(y, axis=1)
        y = np.add(y, self.bias)

        for k in range(len(y)):
            y[i] = self.sigmoid(y[i])

        u = np.multiply(np.transpose(y), self.weights2)
        u = np.sum(u, axis=1)
        u = self.sigmoid(u)

        return u

    def train_weights(self, output, i):

        erro = self.target[i] - self.output
        n = self.learning_rate * erro

        self.bias = self.bias + n

        variation = np.multiply(self.amostras[i, :-1], n)
        self.weights = np.add(variation, self.weights)


    def zera_count(self):
        self.count = 0

    def shuffle(self):
        np.random.shuffle(self.amostras)
        self.target = self.amostras[:, -1]

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def vetor_um_zero(self,valor):
        um_zero = valor
        max = np.max(um_zero)
        for i in range(len(um_zero)):
            if(um_zero[i] == max):
                um_zero[i] = 1
            else:
                um_zero[i] = 0

        return um_zero

    def cria_erro(self, valor):
        #print(valor)
        self.saida_total = np.array([])
        self.saida_total = np.insert(self.saida_total, 0, valor)
        #print(self.saida_total)
