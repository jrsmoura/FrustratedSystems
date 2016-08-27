"""
    Arquivo principal
    author: JR Steiner
    jrsmoura@uesc.br
"""

import matplotlib.pyplot as plt
import numpy as np

import base.InitialContidions.InitialConditions as conf
import base.MonteCarloMove.MonteCarlo as mc
import base.PhysQuant.BasicCalcs as cl
from matplotlib import cm as CM
from matplotlib import mlab as ML



L = 32

mcSteps = 500
eqSteps = 100
T = 2.5

config = conf.ferromagnet(L)

for i in range(eqSteps):
    mc.mcmove(config, 1.0/T, L)
for i in range(mcSteps):
    mc.mcmove(config, 1.0/T, L)   # monte carlo moves


plt.figure(2)
plt.imshow(config, interpolation='bicubic')
plt.grid(True)
plt.colorbar()
plt.show()

print config