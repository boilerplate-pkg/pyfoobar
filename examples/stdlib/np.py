
#%%
import numpy as np
data = np.memmap(file, dtype=np.uint16, mode="r", shape=(800,640,640))