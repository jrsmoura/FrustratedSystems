import numpy as np
import matplotlib.pyplot as plt

import base.InitialContidions.InitialConditions as initial

x = initial.CoupConsts(64)

plt.hist2d(x,  bins = 50)


print x