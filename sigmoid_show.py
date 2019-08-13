#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import math
from xzc_tools import tools
from matplotlib import pyplot as plt

@tools.funcRunTime
def sigmoid_show():
    try:
        x = [i for i in range(-10, 11)]
        y = [1 / (1 + math.exp(-i)) for i in x]
        plt.title("sigmoid")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(x, y)
        plt.show()
    except Exception as msg:
        tools.printInfo(2, msg)

if __name__ == '__main__':
    sigmoid_show()