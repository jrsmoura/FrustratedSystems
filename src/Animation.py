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

L = 64
nt = 256

dpi = 260

mcSteps = 3000
eqSteps = 500

ims =[]
fig = plt.figure()
#temperature
T  = np.linspace(1., 4., nt)
config = conf.ferromagnet(L)


for m in range(len(T)):
    im = plt.imshow(config ,interpolation='lanczos', animated=True)
    ims.append([im])
    config = conf.ferromagnet(L)
    #temalization process
    for i in range(eqSteps):
        mc.mcmove2d(config, 1.0 / T[m], L)
    for i in range(mcSteps):
        # monte carlo moves
        mc.mcmove2d(config, 1.0 / T[m], L)
ani = animation.ArtistAnimation(fig, ims, blit=True, interval=1, repeat_delay=100)
ani.save('dynamic_images.gif')
plt.show()

print 'Cabou .... vai ver se salvou o arquivo cert, mané!'