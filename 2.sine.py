import numpy as np
import matplotlib.pyplot as plot
t=np.arange(0, 30, 0.1)
wave=np.sin(t)
plot.stem(t,wave,'k')
plot.show()

