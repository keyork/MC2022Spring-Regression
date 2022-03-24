
import matplotlib.pyplot as plt
import numpy as np


def draw_sample(data_X, data_y, save_path):

    fig, ax = plt.subplots()
    plt.xlim((0, 11))
    plt.ylim((np.min(data_y)-5, np.max(data_y)+5))
    ax.plot(data_X, data_y, 'ko', markersize=2, label='sample data')
    plt.legend()
    plt.savefig(save_path)
    plt.close()


def draw_regression(w, data_X, data_y, save_path):

    fig, ax = plt.subplots()
    x = np.arange(0, 11, 0.001)
    if w.shape[0] == 2:
        y = w[0, 0]*x + w[-1,0]
    elif w.shape[0] == 3:
        y = w[0, 0]*x + w[1, 0]*(x**2) +w[-1,0]
    elif w.shape[0] == 4:
        y = w[0, 0]*x + w[1, 0]*(x**2) + w[2, 0]*(x**3) + w[-1,0]
    elif w.shape[0] == 5:
        y = w[0, 0]*x + w[1, 0]*(x**2) + w[2, 0]*(x**3) + w[3, 0]*(x**4) + w[-1,0]
    elif w.shape[0] == 6:
        y = w[0, 0]*x + w[1, 0]*(x**2) + w[2, 0]*(x**3) + w[3, 0]*(x**4) + w[4, 0]*(x**5) + w[-1,0]
    plt.xlim((0, 11))
    plt.ylim((np.min(data_y)-5, np.max(data_y)+5))
    ax.plot(data_X, data_y, 'ko', markersize=2, label='sample data')
    ax.plot(x, y, 'b', label='regression result')
    plt.legend()
    plt.savefig(save_path)
    plt.close()


def draw_compare(w_good, w_bad, data_X, data_y, data_y_bad, save_path):

    fig, ax = plt.subplots()
    plt.xlim((0, 11))
    plt.ylim((np.min(data_y_bad)-5, np.max(data_y_bad)+5))
    ax.plot(data_X, data_y, 'ko', markersize=2, label='sample data')
    x = np.arange(0, 11, 0.001)
    is_good = True
    for w in [w_good, w_bad]:
        if w.shape[0] == 2:
            y = w[0, 0]*x + w[-1,0]
        elif w.shape[0] == 3:
            y = w[0, 0]*x + w[1, 0]*(x**2) +w[-1,0]
        elif w.shape[0] == 4:
            y = w[0, 0]*x + w[1, 0]*(x**2) + w[2, 0]*(x**3) + w[-1,0]
        elif w.shape[0] == 5:
            y = w[0, 0]*x + w[1, 0]*(x**2) + w[2, 0]*(x**3) + w[3, 0]*(x**4) + w[-1,0]
        elif w.shape[0] == 6:
            y = w[0, 0]*x + w[1, 0]*(x**2) + w[2, 0]*(x**3) + w[3, 0]*(x**4) + w[4, 0]*(x**5) + w[-1,0]
        if is_good:
            ax.plot(x, y, 'b', label='without bad value')
            is_good = False
        else:
            ax.plot(x, y, 'r', label='contain bad value')
    plt.legend()
    plt.savefig(save_path)
    plt.close()