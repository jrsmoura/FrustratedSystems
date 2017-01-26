#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Arquivo para geração de animações
    author: JR Steiner
    jrsmoura@uesc.br
    date: 27/08/2016
"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colorbar

import base.InitialContidions.InitialConditions as conf
import base.MonteCarloMove.MonteCarlo as mc

L = 8
nt = 512

dpi = 120

mcSteps = 4000
eqSteps = 3000

ims =[]
fig = plt.figure()
#temperature
#T  = np.linspace(.9, 1., nt)
T = 2.0

config = conf.ferromagnet(L)
#config = conf.threestates(L)

#temalization process
#for i in range(eqSteps):
#    mc.mcmove2d(config, 1.0 / T, L)
for i in range(mcSteps):
    # monte carlo moves
    mc.mcmove2d(config, 1.0 / T, L)
    im = plt.imshow(config, interpolation='lanczos', animated=True)
ims.append([im])
ani = animation.ArtistAnimation(fig, ims, blit=True, interval=1, repeat_delay=100)
ani.save('6_BaixaT_5000Passos.gif')
plt.show()

print 'Cabou .... vai ver se salvou o arquivo cert, mané!'
