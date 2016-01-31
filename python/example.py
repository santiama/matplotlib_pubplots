import matplotlib.pylab as plt
import numpy as np
from set_plot_params import plot_multi_format


def example_plot1():
    fig = plt.figure(figsize=(4, 3))
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(1., 8., 30)
    ax.plot(x, x ** 1.5, color='k', ls='solid')
    ax.plot(x, 20/x, color='0.50', ls='dashed')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (K)')
    fig.tight_layout()
    return [fig], ['example_1']


if __name__ == '__main__':

    fig_funcs = [example_plot1]
    plot_multi_format(fig_funcs)
