import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from scipy.interpolate import make_interp_spline, BSpline


def set_weigth_mes():
    weigth = []

    # Jan ~ (4.2 - 5.5)
    # Fer ~ (3.6 - 4.4)
    # Mar ~ (2.6 - 3.4)
    # Abr ~ (3.4 - 4.2)
    # Mai ~ (2.2 - 2.8)
    # Jun ~ (1.8 - 2.6)
    # Jul ~ (3.6 - 4.4)
    # Ago ~ (2.6 - 3.4)
    # Set ~ (2.0 - 2.8)
    # Out ~ (3.0 - 3.8)
    # Nov ~ (3.6 - 4.4)
    # Dez ~ (4.6 - 5.2)

    for i in range(12):
        if i == 0:
            weigth.append(np.random.uniform(4.2, 5.0))
        if i == 1:
            weigth.append(np.random.uniform(3.6, 4.4))
        if i == 2:
            weigth.append(np.random.uniform(2.6, 3.4))
        if i == 3:
            weigth.append(np.random.uniform(3.4, 4.2))
        if i == 4:
            weigth.append(np.random.uniform(2.2, 2.8))
        if i == 5:
            weigth.append(np.random.uniform(1.8, 2.6))
        if i == 6:
            weigth.append(np.random.uniform(2.6, 4.4))
        if i == 7:
            weigth.append(np.random.uniform(3.6, 3.4))
        if i == 8:
            weigth.append(np.random.uniform(2.0, 2.8))
        if i == 9:
            weigth.append(np.random.uniform(3.0, 3.8))
        if i == 10:
            weigth.append(np.random.uniform(3.6, 4.4))
        if i == 11:
            weigth.append(np.random.uniform(4.6, 5.2))

    # print(weigth, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    return weigth


def set_qnt_UF_mes(n_anos):
    UF_mes = []
    messes = []
    weigth = []

    for i in range(26):
        weigth = set_weigth_mes()
        weight = np.array(weigth) * 2
        for j in range(n_anos * 12):
            qnt = np.random.randint(35, 85)
            valor = float("{0:.2f}".format(qnt * weigth[j % 12]))
            messes.append(valor)
        UF_mes.insert(i, messes)
        messes = []

    # print(UF_mes, "\n\n\n")
    return UF_mes


if __name__ == '__main__':

    empresas = []
    produtos = []
    UF_mes = []

    # n_empresas = int(input())
    # n_produtos = int(input())
    # n_anos = int(input())
    n_empresas = 1
    n_produtos = 2
    n_anos = 5

    for i in range(n_empresas):
        for j in range(n_produtos):
            produtos.append(set_qnt_UF_mes(n_anos))
        empresas.append(produtos)

    T = [0] * (n_anos * 12)

    for i in range(len(empresas)):
        for j in range(len(empresas[i])):
            print("\nProcuto {}\n".format(j + 1))
            for k in range(len(empresas[i][j])):
                T = np.add(empresas[i][j][k], T)
            list_x = [c for c in range(len(T))]
            list_y = T
            plt.figure()
            poly = np.polyfit(list_x,list_y,7)
            poly_y = np.poly1d(poly)(list_x)
            plt.plot(list_x,poly_y)
            plt.plot(list_x,list_y)
            plt.show()
