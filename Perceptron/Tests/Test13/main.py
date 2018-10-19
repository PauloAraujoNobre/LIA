import redeneural
from redeneural import RedeNeural
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
    Amostras = pd.read_csv(nome + '.csv', header=None)
    amostras = Amostras.copy()
    amostras = amostras.values  # Pandas -> Normal
    amostras = np.matrix(amostras)  #Normal -> Numpy
    return amostras

class main:
    amostras = criaMatrix("Amostras")

    np.random.shuffle(amostras)

    [row, col] = amostras.shape
    target = amostras[:, -1].copy()

    amostras = normalizar(col, amostras)

    rowTotal = row
    row = int(row * 0.8)

    amostrasPerceptron = amostras[:row, :].copy()
    amostrasTeste = amostras[row:, :].copy()
    targetTeste = amostrasTeste[:, -1].copy()

    RedeNeural = RedeNeural(amostrasPerceptron, target)
    (weights, epoch) = RedeNeural.train()

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
