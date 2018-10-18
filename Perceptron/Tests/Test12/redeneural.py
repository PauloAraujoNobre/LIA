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
        self.targetDegrau = [0.01, 0.99]
        self.saida_total = np.array([])
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
                self.output = self.predict(i).copy()
                vetor_um_zero = self.vetor_um_zero(self.output)

                erroTotal = self.cria_erro_total(vetor_um_zero)
                self.backPropagation()

            self.epoch += 1
        return (self.weights, self.epoch)

    def predict(self, i):
        linha = self.amostras[i, :]
        linha = linha[:, :-1]
        #print(linha)            #a = [x1, x2]
        #print(self.weights1)    #w = [[w11, w21][w12, 22][w13, w23]]
        self.y = np.multiply(linha, self.weights1)
        self.y = np.sum(self.y, axis=1)
        self.y = np.add(self.y, self.bias)

        for k in range(len(self.y)):
            self.y[i] = self.sigmoid(self.y[i])

        u = np.multiply(np.transpose(self.y), self.weights2)
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
        um_zero = valor.copy()
        max = np.max(um_zero)
        for i in range(len(um_zero)):
            if(um_zero[i] == max):
                um_zero[i] = 1
            else:
                um_zero[i] = 0

        return um_zero

    def cria_erro_total(self, vetor_um_zero):
        erroTotal = 0
        output = np.array(np.transpose(self.output)).copy()
        for k in range(len(self.output)):
            if vetor_um_zero[k] != self.targetDegrau[k]:
                erroTotal += 0.5 * pow(output[0, k] - self.targetDegrau[k], 2)
        return erroTotal

    def backPropagation(self):
        output = np.array(np.transpose(self.output)).copy()
        d1 = output[0, 0] - self.targetDegrau[0]
        d2 = output[0, 0] * (1 - output[0, 0])
        d3 = self.y[0]
        dt = d1 * d2 * d3




        #print(self.weights2[0, 0] + dt * self.learning_rate)
        #print("print \n")
        n = dt * self.learning_rate
        a = self.weights2[0, 0] + n
        self.weights2[0, 0] = a.copy()

        print(self.weights2[0, 0])
        print("saida\n")
        print(n)
        print("nn\n")
