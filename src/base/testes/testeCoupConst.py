import numpy as np
import matplotlib.pyplot as plt

import base.InitialContidions.InitialConditions as initial

x = initial.CoupConsts(64)

y = np.split(x, 2)


print y