import numpy as np

## Energy calculation
def calcEnergy(config, N):
    energy = 0
    for i in range(len(config)):
        for j in range(len(config)):
            S = config[i,j]
            nb = config[(i+1)%N, j] + config[i,(j+1)%N] + config[(i-1)%N, j] + config[i,(j-1)%N]
            energy += -nb*S
    return energy/4.

## magnetization of  the configuration

def calcMag(config):
    mag = np.sum(config)
    return mag