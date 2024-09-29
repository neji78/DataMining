import numpy as np
from numpy import random
randomData=random.randint(1,1000, size=(700))
np.save('PreparingData/data', randomData)