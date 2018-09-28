import variable
from variable import Variable
import perceptron
from perceptron import Perceptron
import numpy as np
from numpy import genfromtxt
import random
import copy
import tkinter
import matplotlib.pyplot as plt

class main:

    Amostras = np.genfromtxt('Amostras.csv', delimiter=',')
    amostras = Amostras.copy()
    target = amostras[:, 0].copy()
    amostras[:, 0] = 1
    [row, col] = amostras.shape
    weights = np.random.rand(col)
    learning_rate = np.random.uniform(0.01, 0.05)
    epoch = 0

    Perceptron = Perceptron(amostras, target, weights, epoch, row, col, learning_rate)
    (weights, epoch) = Perceptron.train()

    print("Os pesos equivalem a {}".format(weights))
    print("Foram necessarias {} epocas".format(epoch))

    Dados = np.genfromtxt('Amostras.csv', delimiter=',')
    dados = Dados.copy()
    dados[:, 0] = 1
    [rowD, colD] = dados.shape
    for i in range(rowD):
        u = np.dot(dados[i, :], weights)
        if u >= 0:
            output = 1
        else:
            output = 0
        print(output)

    print("Saidas desejadas: {}".format(target))



