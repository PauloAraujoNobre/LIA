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
    weights = np.random.rand(1, col)
    learning_rate = np.random.uniform(0.1, 0.5)
    epoch = 0

    Perceptron = Perceptron(amostras, target, weights, epoch, row, col, learning_rate)
    (weights, epoch) = Perceptron.train()

    print("Os pessos equivalem a {}".format(weights))
    print("Foram necessarias {} epocas".format(epoch))

