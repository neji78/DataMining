import numpy as np
import JsonMaker as jm
import matplotlib.pyplot as plt
dataArray = np.load('PreparingData/data.npy')
minData = np.min(dataArray)
maxData = np.max(dataArray)
rangeData = maxData - minData
standardDeviation = np.std(dataArray)

variance = np.var(dataArray)
jsonMakerObject = jm.Json("PreparingData/MeasuresOfVarince")
jsonMakerObject.add("minData",int(minData))
jsonMakerObject.add("maxData",int(maxData))
jsonMakerObject.add("rangeData",int(rangeData))
jsonMakerObject.add("standardDeviation",standardDeviation)
jsonMakerObject.add("variance",variance)
jsonMakerObject.save()

AConstant = np.sqrt(1/(2*np.pi*standardDeviation**2))
Bx = -(dataArray - np.mean(dataArray))**2/(2*standardDeviation**2)
NoramlDist = AConstant*np.exp(Bx)
plt.bar(dataArray,NoramlDist,width=1)

plt.savefig("PreparingData/normalDistributionOfData.png")