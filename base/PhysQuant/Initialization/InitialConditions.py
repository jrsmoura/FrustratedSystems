import numpy as np


#Ferromagnetic initial condition
def Ferromag(N):  # generates a random spin config
    state = 2 * np.random.randint(2, size=(N, N)) - 1
    return state