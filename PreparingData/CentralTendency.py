import JsonMaker as jm
import numpy as np
from scipy.stats import gmean,hmean,mode
dataArray = np.load('PreparingData/data.npy')
medain = np.median(dataArray)
mean = np.mean(dataArray)
modeData = mode(dataArray, keepdims=True)
geometryMean = gmean(dataArray)
harmonicMean = hmean(dataArray)

jsonMakerObject = jm.Json("PreparingData/CentralTendency")
jsonMakerObject.add("medain",medain)
jsonMakerObject.add("mean",mean)
jsonMakerObject.add("mode",int(modeData.mode[0]))
jsonMakerObject.add("modeCount",int(modeData.count[0]))
jsonMakerObject.add("geometryMean",geometryMean)
jsonMakerObject.add("harmonicMean",harmonicMean)
jsonMakerObject.save()

