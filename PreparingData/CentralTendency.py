import numpy as np
from scipy.stats import gmean,hmean
dataArray = np.load('PreparingData/data.npy')
medain = np.median(dataArray)
mean = np.mean(dataArray)
geometryMean = gmean(dataArray)
harmonicMean = hmean(dataArray)
minData = np.min(dataArray)
maxData = np.max(dataArray)
rangeData = maxData - minData
standardDeviation = np.std(dataArray)