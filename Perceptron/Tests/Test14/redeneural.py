import numpy as np

class RedeNeural():

    def __init__(self, amostras, target):
        self.amostras = amostras
        self.target = target
        self.epoch = 0
        [self.row, self.col] = self.amostras.shape
        #self.learning_rate = np.random.rand(1, 1)
        self.learning_rate = 0.5
        #self.weights1 = np.random.rand(3, 2)
        self.weights1 = np.random.rand(3, 2)
        #self.weights2 = np.random.rand(2, 3)
        self.weights2 = np.random.rand(2, 3)
        self.targetDegrau = [0.01, 0.99]
        self.saida_total = np.array([])
        #print(self.bias)
        #print(self.weights1)
        #print("\n")
        #print(self.weights2)
        #or self.delta_erro < 0.01
    def train(self):
        self.cria_bias()
        self.count = 0
        while (self.epoch < 200):
            self.shuffle()
            self.zera_count()
            for i in range(self.row):
                self.output = self.predict(i).copy()
                vetor_um_zero = self.vetor_um_zero(self.output)

                #erroTotal = self.cria_erro_total(vetor_um_zero)
                self.backPropagation(i)

            self.epoch += 1
        return (self.output)

    def predict(self, i):
        linha = self.amostras[i, :]
        linha = linha[:, :-1]
        print(linha)
        #print(linha)            #a = [x1, x2]
        # print("aa\n")
        # print(self.weights1)    #w1 = [[w11, w21][w12, 22][w13, w23]]
        # print("bb\n")
        self.y = np.multiply(linha, self.weights1)
        # print(self.y)
        # print("\na")
        self.y = np.sum(self.y, axis=1)
        # print(self.y)
        # print("\nb")
        # print(np.transpose(self.bias[0]))
        # print("\na")
        self.y = np.add(self.y, self.bias[0])

        for k in range(len(self.y)):
            self.y[i] = self.sigmoid(self.y[i])

        u = np.multiply(np.transpose(self.y), self.weights2)
        u = np.sum(u, axis=1)
        u = self.sigmoid(u)
        u = np.add(u, self.bias[1])
        # print(u)
        # print("a\n")
        # print(np.transpose(self.bias[1]))
        # print("b\n")

        return u

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

    """
    def cria_erro_total(self, vetor_um_zero):
        erroTotal = 0
        output = np.array(np.transpose(self.output)).copy()
        for k in range(len(self.output)):
            if vetor_um_zero[k] != self.targetDegrau[k]:
                erroTotal += 0.5 * pow(output[0, k] - self.targetDegrau[k], 2)
        return erroTotal
    """
    def cria_bias(self):
        [row, col] = self.weights2.shape

        a = []
        a.append(np.random.random((col, 1)))
        a.append(np.random.random((row, 1)))
        self.bias = a.copy()
        #print(self.bias)
        #print("aa\n")
        #print(self.bias[1][0, 1])



    def backPropagation(self, i):
        i2 = i
        #print(self.output)
        #print("\n")

        [row, col] = self.weights2.shape
        output = np.array(np.transpose(self.output)).copy()

        for i in range(row):
            for j in range(col):
                d1 = output[0, i] - self.targetDegrau[i]
                d2 = output[0, i] * (1 - output[0, i])
                d3 = self.y[j]
                dt = d1 * d2 * d3

                n = dt * self.learning_rate
                self.weights2[i, j] += n

        [row_out, col_out] = output.shape

        # w2 = [[w31, w41, w51], [w32. w42, w52]

        [row, col] = self.weights1.shape
        #print(row)
        #print("aa\n")
        #print(col)
        #print("bb\n")
        #print(self.amostras)
        #print("aa\n")
        #print(self.amostras[1, 2])
        #print("bb\n")
        #print(output)
        #print("aa\n")
        #print(output[0, 1])
        #print("\n")
        #print(self.weights1)
        #print("\na")
        #print(self.weights1[1, 2])
        #print("\nb")

        for i in range(row):
            for j in range(col):
                somad1 = 0
                for k in range(col_out):
                    somad1 += (output[0, k] - self.targetDegrau[k]) * (output[0, k] * (1 - output[0, k])) * self.weights2[k, i]

                d1 = somad1
                d2 = self.y[i] * (1 - self.y[i])
                d3 = self.amostras[i2, j]
                dt = d1 * d2 * d3

                n = dt * self.learning_rate
                self.weights1[i, j] += n

        #BIAS
        #print(self.bias)
        #print(self.bias[1][1])
        #print(self.output)
        #print(self.output[1, 0])

        for i in range(len(self.bias)):
            for j in range(len(self.bias[i])):
                if i == 0:
                    self.bias[i][j] = self.learning_rate * self.y[j] * (1 - self.y[j])
                else:
                    self.bias[i][j] = self.learning_rate * self.output[j, 0] * (1 - self.output[j, 0])
