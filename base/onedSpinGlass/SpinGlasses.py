import numpy as np
from numpy import random as ran


#Ferromagnetic one-dimensional spin-glass with gaussian distribution over couples
#constants
def statenet(N):
    return np.ones(N), ran.normal(0., 1.0, N)

