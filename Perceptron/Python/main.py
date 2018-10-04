import perceptron
from perceptron import Perceptron
import pandas as pd
import numpy as np
from numpy import genfromtxt
import random
import copy
import tkinter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def ploting(amostrasTeste, targetTeste):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(amostrasTeste[:, 0], amostrasTeste[:, 1], amostrasTeste[:, 2], c=targetTeste)
    plt.show()

def normalizar(col, amostras):
    for i in range(col - 1):
        colunaMax = np.max(amostras[:, i])
        colunaMin = np.min(amostras[:, i])

        amostras[:, i] = (np.divide(np.subtract(amostras[:, i], colunaMin), (colunaMax-colunaMin)))
        return amostras

def criaMatrix(nome):
    Amostras = pd.read_csv(nome + '.csv')
    amostras = Amostras.copy()
    amostras = amostras.values  # Pandas -> Normal
    return amostras

class main:
    amostras = criaMatrix("Amostras")

    np.random.shuffle(amostras)

    [row, col] = amostras.shape
    target = amostras[:, -1]
    targetAux1 = target[0]

    for i in range(row):
        if target[i] != targetAux1:
            targetAux2 = target[i]
            break

    amostras[:, -1] = np.where(amostras[:, -1] == targetAux1, 1, -1)

    amostras = normalizar(col, amostras)

    weights = np.random.rand(col-1)
    learning_rate = np.random.uniform(0.01, 0.05)
    epoch = 0
    rowTotal = row
    row = int(row * 0.8)

    amostrasPerceptron = amostras[:row, :].copy()
    amostrasTeste = amostras[row:, :].copy()
    targetTeste = amostrasTeste[:, -1].copy()

    Perceptron = Perceptron(amostrasPerceptron, target, weights, epoch, row, col, learning_rate)
    (weights, epoch) = Perceptron.train()

    weights = np.insert(weights, col-1, Perceptron.bias)

    print("\nOs pesos equivalem a {}".format(weights))
    print("Foram necessarias {} epocas\n".format(epoch))

    dados = amostrasTeste.copy()
    dados[:, -1] = 1
    acerto = 0
    count = 0

    for i in range(rowTotal - row):
        u = np.dot(dados[i, :], weights)
        count += 1

        if u >= 0:
            output = 1
        else:
            output = -1

        if output == targetTeste[i]:
            acerto += 1

        print("Ex: {}".format(count))

        if output == 1:
            print("Saida atual: {}".format(targetAux1))
        else:
            print("Saida atual: {}".format(targetAux2))

        if targetTeste[i] == 1:
            print("Saida desejada: {}\n".format(targetAux1))
        else:
            print("Saida desejada: {}\n".format(targetAux2))


    taxaDeAcerto = acerto / count
    taxaDeAcerto = taxaDeAcerto * 100
    print("A taxa de acerto foi {:.2f}%".format(taxaDeAcerto))

    ploting(amostrasTeste, targetTeste)
