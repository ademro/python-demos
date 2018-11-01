#Defined Packages

#Because numy and pandas is included in the pipfile.lock it will be included in your virtual environment distribution.

import numpy as np
import pandas as pd

#Define numpy array
testArray = np.array([1,2,3,4,5])
#Create an empty dataframe
emptyDf = pd.DataFrame(columns=['Col1','Col2','Col3'])
#Create a series (row) to append to empty df
testSeries = pd.Series({'Col1':1,'Col2':2,'Col3':3})
#append the row onto the dataframe
testDf = emptyDf.append(testSeries,ignore_index=True)
#print results
print(testArray)
print(testDf)
