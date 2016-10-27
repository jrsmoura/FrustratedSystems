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
import base.PhysQuant.BasicCalcs as bc


L = 8

mcSteps = 1000
eqSteps = 8000

ims =[]
fig = plt.figure()

nt = 64
order = np.zeros(nt)

#config = conf.threestates(L)
config = conf.ferromagnet(L)
T = np.linspace(1.0, 4.0, num=nt)

for m in range(len(T)):
    config = conf.ferromagnet(L)
    print "T = ", m
    for i in range(eqSteps):
        mc.mcmove2d(config, 1.0 / T[m], L)

    for i in range(mcSteps):
        mc.mcmove2d(config, 1.0 / T[m], L)   # monte carlo moves
        order[m] = bc.orderParameter(config)
#plt.imshow(config, interpolation='lanczos')
plt.plot(T, order)

plt.show()

print config