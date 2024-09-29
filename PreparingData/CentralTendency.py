import numpy as np
from scipy.stats import gmean,hmean,mode
dataArray = np.load('PreparingData/data.npy')
medain = np.median(dataArray)
mean = np.mean(dataArray)
modeData = mode(dataArray, keepdims=True)
geometryMean = gmean(dataArray)
harmonicMean = hmean(dataArray)

