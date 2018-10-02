import perceptron
from perceptron import Perceptron
import pandas as pd
import numpy as np
from numpy import genfromtxt
import random
import copy
import tkinter
import matplotlib.pyplot as plt

class main:

    Amostras = pd.read_csv('Amostras.csv')
    amostras = Amostras.copy()
    amostras = amostras.values
    [row, col] = amostras.shape
    target = amostras[0:100, 4]
    targetAux1 = target[0]

    for i in range(row):
        if target[i] != targetAux1:
            targetAux2 = target[i]
            break

    target = np.where(target == targetAux1, -1, 1)

    weights = np.random.rand(col)
    learning_rate = np.random.uniform(0.01, 0.05)
    epoch = 0
    rowTotal = row
    row = int(row * 0.8)

    Perceptron = Perceptron(amostras, target, weights, epoch, row, col, learning_rate)
    (weights, epoch) = Perceptron.train()



    print("\nOs pesos equivalem a {}".format(weights))
    print("Foram necessarias {} epocas\n".format(epoch))

    dados = amostras.copy()
    count = 1
    for i in range(rowTotal - row):
        u = np.dot(dados[i, :], weights)
        if u >= 0:
            output = targetAux1
        else:
            output = targetAux2
        print("Ex: {}".format(count))
        print("Saida atual: {}".format(output))
        if target[i] == 1:
            print("Saida desejada: {}\n".format(targetAux1))
        else:
            print("Saida desejada: {}\n".format(targetAux2))
        count += 1
