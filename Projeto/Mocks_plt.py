import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from scipy.interpolate import make_interp_spline, BSpline
from scipy.interpolate import interp1d


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
        weight = np.divide(weigth, 2)
        for j in range(n_anos * 12):
            qnt = np.random.randint(15, 225)
            valor = float("{0:.2f}".format(qnt * weigth[j % 12]))
            messes.append(valor)
        UF_mes.insert(i, messes)
        messes = []

    # print(UF_mes, "\n\n\n")
    return UF_mes


def set_dataset(vetor_prod, n_anos):

    empresas = []
    produtos = []
    UF_mes = []

    n_empresas = len(vetor_prod)
    n_produtos = vetor_prod
    # n_empresas = 2
    # n_produtos = 3
    # n_anos = 1

    for i in range(n_empresas):
        for j in range(vetor_prod[i]):
            produtos.append(set_qnt_UF_mes(n_anos))
        empresas.append(produtos)
        produtos = []

    media = [0] * (n_anos * 12)
    legend = []

    arq1 = open('Mocks.txt', 'w')
    # print("Without Smooth Curve Grafics:")
    for i in range(len(empresas)):
        arq1.write('\nEmpresa {}\n'.format(i + 1))
        # print("\nEmpresa {}\n".format(i+1))
        for j in range(len(empresas[i])):
            arq1.write('\nProduto {}\n'.format(j + 1))
            # print("\nProduto {}\n".format(j+1))
            for k in range(len(empresas[i][j])):
                arq1.write('{}'.format(empresas[i][j][k]))
                #print(empresas[i][j][k])
                media = np.add(empresas[i][j][k], media)
            media = np.divide(media, 26)
            list_x = [c for c in range(len(media))]
            list_y = media
            plt.plot(list_x, list_y)


        plt.title("Amostra de Produtos ao Mês(Without Smooch Curve)")
        plt.xlabel("Messes")
        plt.ylabel("MPE(Média de Produtos de todos Estado)")
        plt.show()
    arq1.close()

    # arq2 = open('WithSmoochCurveGrafics.txt', 'w')
    # print("With Smooch Curve Grafics:")
    for i in range(len(empresas)):
        # arq2.write('\nEmpresa {}\n'.format(i + 1))
        # print("\nEmpresa {}\n".format(i + 1))
        for j in range(len(empresas[i])):
            # arq2.write('\nProduto {}\n'.format(j + 1))
            # print("\nProduto {}\n".format(j+1))
            for k in range(len(empresas[i][j])):
                # arq2.write('{}'.format(empresas[i][j][k]))
                # print(empresas[i][j][k])
                media = np.add(empresas[i][j][k], media)
            media = np.divide(media, 26)
            list_x = [c for c in range(len(media))]
            list_y = media
            tam = len(list_y)
            xnew = np.linspace(1, tam, num=150, endpoint=True)
            x = np.linspace(1, tam, tam)
            f2 = interp1d(x, list_y, kind='cubic')
            plt.plot(xnew, f2(xnew))

        plt.legend(["Produto A", "Produto B", "Produto C"])
        plt.title("Amostra de Produtos ao Mês(With Smooch Curve)")
        plt.xlabel("Messes")
        plt.ylabel("MPE(Média de Produtos de todos Estado)")
        plt.show()

    # arq2.close()
    return empresas

if __name__ == '__main__':

    vetor_prod = [3, 4, 5]
    n_anos = 5
    dataset = set_dataset(vetor_prod, n_anos)
    print(dataset)


