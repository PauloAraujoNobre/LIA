import treino
from treino import Treino
import numpy as np
import random
import copy
import tkinter
import matplotlib.pyplot as plt
class main:

    Amostras = np.genfromtxt('Amostras.csv', delimiter=',')
    amostras = Amostras.copy()
    target = amostras[:,0].copy()
    amostras[:, 0] = 1
    [tamRow,tamCol] = Amostras.shape
    rand = np.random.rand(1, tamCol)
    pesos = rand.copy()
    pesos[:, 0] = random.uniform(-1, 1)
    taxaDeAprend = random.uniform(0, 1)
    epocas = 0;

   # print(pesos)
   # print("\n\n\n")
   # print(amostras)

    t = treino.Treino(pesos, taxaDeAprend, target, tamCol, tamRow, amostras, epocas)
    (pesos, epocas) = t.treinar()
    print("Os pessos equivalem à {}".format(pesos))
    print("Foram necessarias {} epocas".format(epocas))

    plt.scatter(amostras[:, 1], amostras[ :, 2], c=amostras[:, 0])
    plt.title("Setosa x versicolor")
    plt.xlabel('Sepal.Width')
    plt.ylabel('Sepal.Length')
    plt.show()
