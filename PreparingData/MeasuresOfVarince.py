import numpy as np
from scipy.stats import gmean,hmean,mode
import matplotlib.pyplot as plt
dataArray = np.load('PreparingData/data.npy')
minData = np.min(dataArray)
maxData = np.max(dataArray)
rangeData = maxData - minData
standardDeviation = np.std(dataArray)
variance = np.var(dataArray)
AConstant = np.sqrt(1/(2*np.pi*standardDeviation**2))
Bx = -(dataArray - np.mean(dataArray))**2/(2*standardDeviation**2)
NoramlDist = AConstant*np.exp(Bx)
plt.bar(dataArray,NoramlDist,width=1)

plt.savefig("PreparingData/normalDistributionOfData.png")