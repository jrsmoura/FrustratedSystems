import numpy as np
import base.onedSpinGlass.SpinGlasses as gls

N = 8
state = np.zeros(N)
couple = np.zeros(N)

state , couple = gls.statenet(N)

print state, couple

