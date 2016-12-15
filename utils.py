import matplotlib.pyplot as plt
from numpy import random

def generateActionValues(numberOfArms):
    return random.normal(0, 1, numberOfArms);

def plot(*mse):
    for i in mse:
        t = range(1,len(i)+1)
        plt.plot(t, i)

    plt.ylabel('avg_rewards')
    plt.show()