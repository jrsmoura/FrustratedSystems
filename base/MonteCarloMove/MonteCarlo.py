## monte carlo moves

import numpy as np
from numpy.random import rand

def mcmove(config, beta, N):
    for i in range(N):
        a = np.random.randint(0, N)
        b = np.random.randint(0, N)
        s =  config[a, b]
        nb = config[(a+1)%N, b] + config[(a-1)%N, b] + config[a, (b+1)%N] + config[a, (b-1)%N]
        cost = 2*s*nb
        if cost < 0:
            s *= -1
        elif rand() < np.exp(-cost*beta):
            s *= -1
        config[a, b] = s
    return config
