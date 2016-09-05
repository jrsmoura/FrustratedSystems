import numpy as np


# random two states initial condition
def randomstates(L):  # generates a random spin config
    state = 2 * np.random.randint(2, size=(L, L)) - 1
    return state

# Ferromagnetic initiala condition
def ferromagnet(L):
    state = np.matrix(np.ones((L,L)))
    return state

# sistema de 3 niveis: -1, 0, +1
def threestates(L): #TODO
    state = 2 * np.random.randint(3, size=(L, L)) - 1
    return state

#Cnostantes de acoplamentos com distribuicao gaussiana
def CoupConsts(L):
    state = np.random.normal(0, 1.0, size=(L,L))
    return state