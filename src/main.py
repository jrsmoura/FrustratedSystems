#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Arquivo principal -> evolução da temperatura
    author: JR Steiner
    jrsmoura@uesc.br
    date: 28/08/2016
"""

import matplotlib.pyplot as plt
import numpy as np


import base.InitialContidions.InitialConditions as conf
import base.MonteCarloMove.MonteCarlo as mc
import base.PhysQuant.BasicCalcs as cl

#Lattice size
L = 16
#Number of temperatures
nt = 128

mcSteps = 3000
eqSteps = 500
Energy = np.zeros(nt)
Magnetization = np.zeros(nt)
SpecificHeat = np.zeros(nt)
Susceptibility = np.zeros(nt)

#temperature array
T = np.linspace(1., 4., nt)

for m in range(len(T)):
    E1 = M1 = E2 = M2 = 0
    config = conf.ferromagnet(L)
    J = conf.CoupConsts(L)
    #termalization process
    for i in range(eqSteps):
        mc.mcmove(config, 1.0/T[m], L)
    for i in range(mcSteps):
        # monte carlo moves
        mc.mcmove(config, 1.0/T[m], L)
        # calculate the energy
        Ene = cl.calcEnergy(config, L)
        # calculate the magnetisation
        Mag = cl.calcMag(config)

        E1 = E1 + Ene
        M1 = M1 + Mag
        M2 = M2 + Mag*Mag ;
        E2 = E2 + Ene*Ene;

        Energy[m] = E1/(mcSteps*L*L)
        Magnetization[m] = M1/(mcSteps*L*L)
        SpecificHeat[m] = ( E2/mcSteps - E1*E1/(mcSteps*mcSteps) )/(L*T[m]*T[m]);
        Susceptibility[m] = ( M2/mcSteps - M1*M1/(mcSteps*mcSteps) )/(L*T[m]*T[m]);

#plot the energy and Magnetization
f = plt.figure(figsize=(18, 10), dpi=80, facecolor='w', edgecolor='k');

sp =  f.add_subplot(2, 2, 1 );
plt.plot(T, Energy, 'o', color="#A60628", label=' Energy');
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Energy ", fontsize=20);

sp =  f.add_subplot(2, 2, 2 );
plt.plot(T, abs(Magnetization), '*', label='Magnetization');
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Magnetization ", fontsize=20);


sp =  f.add_subplot(2, 2, 3 );
plt.plot(T, SpecificHeat, 'd', color="black", label='Specific Heat');
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Specific Heat ", fontsize=20);


sp =  f.add_subplot(2, 2, 4 );
plt.plot(T, Susceptibility, '+', color="green", label='Specific Heat');
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Susceptibility", fontsize=20);

plt.show()

print 'Fim da Simulação'