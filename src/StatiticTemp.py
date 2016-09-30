"""
    Calcula os parametros fisicos a uma temperatura fixa
    author: JR Steiner
    jrsmoura@uesc.br
    date: 27/08/2016
"""

import matplotlib.pyplot as plt
import numpy as np

import base.InitialContidions.InitialConditions as conf
import base.MonteCarloMove.MonteCarlo as mc



L = 128

mcSteps = 5000
eqSteps = 3000
T = 2.32

config = conf.ferromagnet(L)

for i in range(eqSteps):
    mc.mcmove2d(config, 1.0 / T, L)
plt.figure(2)
#plt.imshow(config, interpolation='bicubic')
plt.imshow(config, interpolation='lanczos', animated=True)
plt.grid(True)
#plt.colorbar()
plt.show()


for i in range(mcSteps):
    mc.mcmove2d(config, 1.0 / T, L)   # monte carlo moves

plt.figure(2)
#plt.imshow(config, interpolation='bicubic')
plt.imshow(config, interpolation='lanczos', animated=True)
plt.grid(True)
#plt.colorbar()
plt.show()


print config