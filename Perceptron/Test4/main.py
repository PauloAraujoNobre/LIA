import treino
from treino import Treino
import numpy as np
import random
import copy

class main:

    Amostras = np.genfromtxt('Amostras.csv', delimiter=',')
    amostras = Amostras.copy()
    target = amostras[:,0].copy()
    amostras[:,0] = 0
    [tamCol, tamRow] = Amostras.shape
    rand = np.random.rand(1, tamCol)
    pesos = rand.copy()
    pesos[:, 0] = 0
    print(pesos)
    taxaDeAprend = random.uniform(0, 1)
    epocas = 0;
    t = treino.Treino(pesos, taxaDeAprend, target, tamCol, tamRow, amostras, epocas)
    (pesos, epocas) = t.treinar()
    print("Os pessos equivalem à {}".format(pesos))
    print("Foram necessarias {} epocas".format(epocas))

