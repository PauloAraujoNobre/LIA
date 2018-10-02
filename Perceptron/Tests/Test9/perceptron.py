import numpy as np


class Perceptron():

    def __init__(self, amostras, target, weights, epoch, row, col, learning_rate):
        self.amostras = amostras
        self.target = target
        self.weights = weights
        self.epoch = epoch
        self.row = row
        self.col = col
        self.learning_rate = learning_rate
        self.weights[col-1] = 1

    def train(self):

        self.count = 0
        while self.count != self.row:
            self.zera()
            for i in range(self.row):
                #self.amostras = np.random.shuffle(self.amostras)
                self.shuffle()
                output = self.predict(i)

                if (output != self.target[i]):
                    self.train_weights(output, i)
                else:
                    self.count += 1

            self.epoch += 1
        return (self.weights, self.epoch)

    def predict(self, i):

        u = np.multiply(self.weights, self.amostras[i, :])
        activation = np.sum(u)
        if activation >= 0:
            return 1
        else:
            return -1

    def train_weights(self, output, i):

        erro = self.target[i] - output
        n = self.learning_rate * erro

        variation = np.multiply(self.amostras[i, :], n)
        self.weights = np.add(variation, self.weights)

    def zera(self):
        self.count = 0

    def shuffle(self):
        self.target = self.amostras[:, -1]
        targetAux1 = target[0]
        for i in range(row):
            if target[i] != targetAux1:
                targetAux2 = target[i]
                break

        target = np.where(target == targetAux1, -1, 1)
        print(self.target)
