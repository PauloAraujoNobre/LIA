import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from scipy.interpolate import make_interp_spline, BSpline


def set_weigth_mes():
    weigth = []

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


    return weigth


def set_qnt_UF_mes(n_anos):
    UF_mes = []
    messes = []
    weigth = []

    for i in range(26):
        weigth = set_weigth_mes()
        weight = np.divide(weigth, 5)
        for j in range(n_anos * 12):
            qnt = np.random.randint(15, 125)
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
    n_produtos = 1
    n_anos = 3

    for i in range(n_empresas):
        for j in range(n_produtos):
            produtos.append(set_qnt_UF_mes(n_anos))
        empresas.append(produtos)
        produtos = []

    media = [0] * (n_anos * 12)

    for i in range(len(empresas)):
        for j in range(len(empresas[i])):
            #print("\nProcuto {}\n".format(j + 1))
            for k in range(len(empresas[i][j])):
                #print(empresas[i][j][k])
                media = np.add(empresas[i][j][k], media)
            media = np.divide(media, 26)
            list_x = [c for c in range(len(media))]
            list_y = media
            poly = np.polyfit(list_x, list_y, 7)
            poly_y = np.poly1d(poly)(list_x)
            plt.plot(list_x,poly_y)
            plt.plot(list_x, list_y)
            plt.title("Amostra de Produtos ao Mês")
            plt.xlabel("Messes")
            plt.ylabel("Produtos")
        plt.show()
