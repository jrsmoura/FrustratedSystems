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



L = 64

mcSteps = 10000
eqSteps = 3000
T = 2.5

ims =[]
fig = plt.figure()

config = conf.threestates(L)
#config = conf.ferromagnet(L)
#config = conf.randomstates(L)

for i in range(eqSteps):
    mc.mcmove2d(config, 1.0 / T, L)

for i in range(mcSteps):
    print "mcStep = ", i
    mc.mcmove2d(config, 1.0 / T, L)   # monte carlo moves
#    im = plt.imshow(config, interpolation='lanczos', animated=True)
#   ims.append([im])
#ani = animation.ArtistAnimation(fig, ims, blit=True, interval=1, repeat_delay=100)
#ani.save('6_BaixaT_512Passos.gif')

plt.imshow(config, interpolation='lanczos')
plt.savefig("t4_l64.png")

plt.show()

#print config
