import numpy as np


# random two states initial condition
def randomstates(L):  # generates a random spin config
    state = 2 * np.random.randint(2, size=(L, L)) - 1
    return state

# Ferromagnetic initiala condition
def ferromagnet(L):
    state = np.matrix(np.ones((L,L)))
    return state

def threestates(L):
    state = 2 * np.random.randint(3, size=(L, L)) - 1