"""
    Arquivo principal
    author: JR Steiner
    jrsmoura@uesc.br
"""

import numpy as np
import base.PhysQuant.Initialization.InitialConditions as conf

L = 8

config = conf.ferromagnet(L)

print config