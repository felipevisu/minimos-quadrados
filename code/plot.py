import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from array_operations import transposed_array

def autolabel(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('', xy=(rect.get_x() + rect.get_width() / 2, height))


# Plota um gráfico de colunas para o MMQ de múltiplas variáveis
def plot(values, n):
    values = transposed_array(values)
    data = values[-2]
    regression = values[-1]

    x = np.arange(n)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, data[:n], width, label='Dados')
    rects2 = ax.bar(x + width/2, regression[:n], width, label='Regressão')

    ax.set_ylabel('Milhas por galão')
    ax.set_xlabel('Carros')
    ax.set_title('Regressão múltipla para %i dados aleatórios' % n)
    ax.legend()

    autolabel(ax, rects1)
    autolabel(ax, rects2)

    fig.tight_layout()

    plt.show()


# Plota um gráfico de pontos e reta para o MMQ de uma variável
def single_plot(data, title='Regressão Linear Simples', xlabel=None):
    data.sort(key = lambda data: data[1])
    data = transposed_array(data)

    plt.plot(data[1], data[-2], 'ro', label='Dados')
    plt.plot(data[1], data[-1], label='Regressão')
    plt.title(title)
    plt.ylabel('Milhas por galão')
    if xlabel:
        plt.xlabel(xlabel)
    plt.show()