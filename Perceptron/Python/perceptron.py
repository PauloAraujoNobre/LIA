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

    def train(self):
        self.bias = 1
        self.count = 0
        while self.count != self.row:
            self.count = 0
            self.zera()
            for i in range(self.row):
                self.shuffle()
                output = self.predict(i)

                if (output != self.target[i]):
                    self.train_weights(output, i)
                else:
                    self.count += 1

            self.epoch += 1
        return (self.weights, self.epoch)

    def predict(self, i):
        u = np.multiply(self.weights, self.amostras[i, :(self.col-1)])
        activation = (np.sum(u) + self.bias)
        if activation >= 0:
            return 1
        else:
            return -1

    def train_weights(self, output, i):

        erro = self.target[i] - output
        n = self.learning_rate * erro

        self.bias = self.bias + n

        variation = np.multiply(self.amostras[i, :-1], n)
        self.weights = np.add(variation, self.weights)


    def zera(self):
        self.count = 0

    def shuffle(self):
        np.random.shuffle(self.amostras)
        self.target = self.amostras[:, -1]
