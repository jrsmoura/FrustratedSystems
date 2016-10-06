"""
    Calcula os parametros fisicos a uma temperatura fixa
    author: JR Steiner
    jrsmoura@uesc.br
    date: 27/08/2016
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import base.InitialContidions.InitialConditions as conf
import base.MonteCarloMove.MonteCarlo as mc



L = 16

mcSteps = 5000
eqSteps = 3000
T = 0.000001

ims =[]
fig = plt.figure()

config = conf.threestates(L)

for i in range(eqSteps):
    mc.mcmove2d(config, 1.0 / T, L)

for i in range(mcSteps):
    mc.mcmove2d(config, 1.0 / T, L)   # monte carlo moves
    im = plt.imshow(config, interpolation='lanczos', animated=True)
    ims.append([im])
ani = animation.ArtistAnimation(fig, ims, blit=True, interval=1, repeat_delay=100)
ani.save('6_BaixaT_512Passos.gif')
plt.show()

print config