import numpy as np
from numpy import random as ran


#Ferromagnetic one-dimensional spin-glass
def onedspinglass(N):
    state = np.ones(N)
    couples = ran.normal(0., 1.0, N)
    return state, couples

