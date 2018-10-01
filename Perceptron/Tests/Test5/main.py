import treino
from treino import Treino
import numpy as np
import random
import copy
import tkinter
import matplotlib.pyplot as plt
class main:

    Amostras = np.genfromtxt('Amostras.csv', delimiter=',')
    [tamCol,tamRow] = Amostras.shape

    tamColParcial = int(tamCol * 0.8)
    tamColTeste = tamCol - tamColParcial

    testes = Amostras[tamColParcial:].copy()



    amostras = Amostras[: tamColParcial].copy()
    target = amostras[:, 0].copy()
    amostras[:, 0] = 1

    print(Amostras)
    print(amostras)
    print(testes)

    pesos = np.random.rand(tamRow)
    #pesos = random.uniform(-1, 1)
    taxaDeAprend = random.uniform(0.1, 0.5)
    epocas = 0;

    print(pesos)
    t = treino.Treino(pesos, taxaDeAprend, target, tamColParcial, tamRow, amostras, epocas)
    (pesos, epocas) = t.treinar()


    print("Os pessos equivalem à {}".format(pesos))
    print("Foram necessarias {} epocas".format(epocas))

    somaTotal = 0
    for i in range(tamColParcial):
        somaTotal += sum(np.multiply(amostras[i],pesos))


    t.testar(testes)

    fig = plt.figure()
    ax = plt.axes()

    x = np.linspace(-100, 100, 1000)

    plt.xlim(-1,5 )
    plt.ylim(-1,5);
    ax.plot(x,float(somaTotal) * x + pesos[0],linestyle=':')


    plt.scatter(amostras[:, 1], amostras[ :, 2], c = target
                )
    plt.title("Amostras")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

