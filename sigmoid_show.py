#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import math
import numpy as np
from matplotlib import pyplot as plt

x = [i for i in range(-10, 11)]

y = [1/(1 + math.exp(-i)) for i in x]

plt.title("sigmoid")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.show()


