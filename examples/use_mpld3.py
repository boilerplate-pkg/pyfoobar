

## 
# https://nbviewer.jupyter.org/github/jakevdp/mpld3/blob/master/notebooks/mpld3_demo.ipynb

#%%
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

#%%
# Scatter points
fig, ax = plt.subplots()
np.random.seed(0)
x, y = np.random.normal(size=(2, 200))
color, size = np.random.random((2, 200))

ax.scatter(x, y, c=color, s=500 * size, alpha=0.3)
ax.grid(color='lightgray', alpha=0.7)

#%%
import mpld3
mpld3.display(fig)

#%%
