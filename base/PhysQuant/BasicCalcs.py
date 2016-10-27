import numpy as np

## Energy calculation
def calcEnergy(config, L):
    energy = 0
    for i in range(len(config)):
        for j in range(len(config)):
            S = config[i,j]
            nb = config[(i+1)%L, j] + config[i,(j+1)%L] + config[(i-1)%L, j] + config[i,(j-1)%L]
            energy += -nb*S
    return energy/4.

## magnetization of  the configuration

def calcMag(config):
    mag = np.sum(config)
    return mag

# Order parameter calcularion
def orderParameter(config):
    n1, n2 = .0, .0
#    newConf = np.squeeze(np.asarray(config))
    for i in range(len(config)):
        if (config[i].any() == 1.):
            n1 += 1.
        else:
            n2 += 1.
    return np.abs(n1 - n2)/float(n1 + n2)