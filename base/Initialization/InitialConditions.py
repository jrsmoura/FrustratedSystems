import numpy as np


# Antiferromagnetic initial condition
def antiferromag(L):  # generates a random spin config
    state = 2 * np.random.randint(2, size=(L, L)) - 1
    return state

# Ferromagnetic initiala condition
def ferromagnet(L):
    state = np.ones((L,L))
    return state