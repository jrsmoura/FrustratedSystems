## monte carlo moves

import numpy as np
from numpy.random import rand

def mcmove(config, beta, L):
    for i in range(L):
        a = np.random.randint(0, L)
        b = np.random.randint(0, L)
        s =  config[a, b]
        nb = config[(a+1)%L, b] + config[(a-1)%L, b] + config[a, (b+1)%L] + config[a, (b-1)%L]
        cost = 2*s*nb
        if cost < 0:
            s *= -1
        elif rand() < np.exp(-cost*beta):
            s *= -1
        config[a, b] = s
    return config
