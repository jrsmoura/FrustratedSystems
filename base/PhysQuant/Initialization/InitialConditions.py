import numpy as np


#Ferromagnetic initial condition
def Ferromag(L):  # generates a random spin config
    state = 2 * np.random.randint(2, size=(L, L)) - 1
    return state