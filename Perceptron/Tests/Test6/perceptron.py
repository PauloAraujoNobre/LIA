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
        self.bias = self.weights[:, 0]

    def train(self):

        for i in range(self.row):
            flag = 1
            while flag == 1:
                output = self.predict(i)
                if (output != self.target[i]):
                    self.train_weights(output, i)
                else:
                    flag = 0
                self.epoch += 1
        return (self.weights, self.epoch)

    def predict(self, i):

        u = np.multiply(self.amostras[i, :], self.weights)
        activation = np.sum(u) + self.bias
        if activation >= 0:
            return 1
        else:
            return -1

    def train_weights(self, output, i):

        erro = self.target[i] - output
        n = self.learning_rate * erro

        variation = np.multiply(self.amostras[i, :], n)
        self.weights += variation

        self.bias += n
