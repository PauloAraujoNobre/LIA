import perceptron
from perceptron import Perceptron
import numpy as np
from numpy import genfromtxt
import random
import copy
import tkinter
import matplotlib.pyplot as plt

class main:

    #Inicialização de variaveis
    Amostras = np.genfromtxt('Amostras.csv', delimiter=',')
    amostras = Amostras.copy()
    target = amostras[:, 0].copy()
    amostras[:, 0] = 1
    [row, col] = amostras.shape
    rowTotal = row
    row = int(row * 0.8)
    weights = np.random.rand(col)
    learning_rate = np.random.uniform(0.01, 0.05)
    epoch = 0

    #Função que inicializa e chama o perceptron
    Perceptron = Perceptron(amostras, target, weights, epoch, row, col, learning_rate)
    (weights, epoch) = Perceptron.train()

    #Prints do resultado do treino
    print("\nOs pesos equivalem a {}".format(weights))
    print("Foram necessarias {} epocas\n".format(epoch))

    #Função para testar o resultado do perceptron com outros dados
    dados = Amostras.copy()
    dados[:, 0] = 1
    [rowD, colD] = dados.shape
    count = 1
    for i in range(rowTotal - row):
        u = np.dot(dados[i, :], weights)
        if u >= 0:
            output = 1
        else:
            output = 0
        print("Ex: {}".format(count))
        print("Saida atual {}".format(output))
        print("Saida desejada {}\n".format(target[i]))
        count += 1


