import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
from numpy import exp, log

# activation
def Sigmoid(x):
    return 1.0 / (1.0 + exp(-x))

def Tanh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

def Relu(x):
    return np.array([0 if xx<0 else xx for xx in x])

def Leaky_Relu(x, alpha=0.1):
    return np.array([alpha*xx if xx<0 else xx for xx in x])

def Elu(x, alpha=1.0):
    return np.array([alpha*(exp(xx)-1) if xx<0 else xx for xx in x])

def Softplus(x):
    return log(1 + exp(x))

def Softsign(x):
    return x / (1.0 + abs(x))
    
##################################################################
# activation derivative
def Sigmoid_deriv(x):
    return Sigmoid(x) * (1.0 - Sigmoid(x))

def Tanh_deriv(x):
    return 1.0 - Tanh(x) * Tanh(x)

def Relu_deriv(x):
    return np.array([1 if xx > 0 else 0 for xx in x])

def Leaky_Relu_deriv(x, alpha=0.1):
    return np.array([1 if xx > 0 else alpha for xx in x])

def Elu_deriv(x, alpha=1.0):
    return np.array([1 if xx > 0 else alpha*exp(xx) for xx in x])

def Softplus_deriv(x):
    return exp(x) / (1.0 + exp(x))

def Softsign_deriv(x):
    return 1.0 / (1 + abs(x))**2

def plot_activation(x, y, y_deriv, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x,y, label = title)
    ax.plot(x,y_deriv, label = title + '_deriv')
    ax.grid()
    ax.xaxis.set_major_locator(mtick.MultipleLocator(1.0))
    ax.set_title(title, fontsize = 20)
    ax.spines['top'].set(visible = False);
    ax.spines['right'].set(visible = False);
    ax.spines['bottom'].set(lw = 1, position = ('data',0));
    ax.spines['left'].set(lw = 1, position = ('data',0));
    ax.legend()
    fig.savefig(title + '.png')


if __name__ == '__main__':
    x = np.linspace(-5, 5, 400)

    plot_activation(x, Sigmoid(x), Sigmoid_deriv(x), 'Sigmoid')
    plot_activation(x, Tanh(x), Tanh_deriv(x), 'Tanh')
    plot_activation(x, Relu(x), Relu_deriv(x), 'ReLu')
    plot_activation(x, Leaky_Relu(x), Leaky_Relu_deriv(x), 'Leaky ReLu')
    plot_activation(x, Elu(x), Elu_deriv(x), 'Elu')
    plot_activation(x, Softplus(x), Softplus_deriv(x), 'Softplus')
    plot_activation(x, Softsign(x), Softsign_deriv(x), 'Softsign')


