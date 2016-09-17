"""
    Calcula os parâmetros físicos a uma temperatura fixa
    author: JR Steiner
    jrsmoura@uesc.br
    date: 27/08/2016
"""

import matplotlib.pyplot as plt
import numpy as np

import base.InitialContidions.InitialConditions as conf
import base.MonteCarloMove.MonteCarlo as mc



L = 32

mcSteps = 500
eqSteps = 100
T = 2.5

config = conf.ferromagnet(L)

for i in range(eqSteps):
    mc.mcmove2d(config, 1.0 / T, L)
for i in range(mcSteps):
    mc.mcmove2d(config, 1.0 / T, L)   # monte carlo moves


plt.figure(2)
plt.imshow(config, interpolation='bicubic')
plt.grid(True)
plt.colorbar()
plt.show()

print config