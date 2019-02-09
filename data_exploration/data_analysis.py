#Step 0a ---- Initialize Required Packages

import sqlite3
import csv
import re
import sys
import os
import re
import pandas as pd
from pandas import DataFrame
import numpy as np
import time
pd.options.display.max_colwidth=1000
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',None)
#Sets directory path of the .py file
curDir=os.path.abspath(os.path.dirname('__file__'))

#Step 0b ---- Establish the feed file and processed files location (where the application looks)

feedFileLocation='FeedFiles/'
processedFileLocation='ProcessedFiles/'

#------------------- Establish Local Functions ---------------------------------------

#load a Pipe Delimited File
def loadDATfile(datFile):
    df=pd.DataFrame(pd.read_csv(os.path.join(curDir,feedFileLocation+datFile),header=0,delimiter='|',error_bad_lines=False,dtype=str))
    return df

#load a Tab Delimited File
def loadTabFile(tabFile):
    df=pd.DataFrame(pd.read_csv(os.path.join(curDir,feedFileLocation+tabFile),header=1,delimiter='\t',error_bad_lines=False,dtype=str,))
    return df

#load a Comma Seperated File
def loadCSVfile(csvFile):
    df=pd.DataFrame(pd.read_csv(os.path.join(curDir,feedFileLocation+csvFile),header=0,delimiter=',',error_bad_lines=False,dtype=str))
    return df

def csvFileSave(arrayName,fileName):
    import sqlite3,csv,re,sys
    import pandas as pd
    from pandas import DataFrame
    import numpy as np
    table=DataFrame(arrayName)
    table.to_csv(os.path.join(curDir,processedFileLocation+fileName),index=False,sep=',',)

#Step 1 ---- Load the Data into a DataFrame

analysisDf = loadCSVfile('example_file.csv')

#Step 2 ---- Take a look at your data set

#---2a check out the first 20 rows

    analysisDf_20=analysisDf.head(20)
    analysisDf_20

#---2b check out the last 20 rows

    analysisDf.tail(20)

#---2c check out the length of your data set

    len(analysisDf)

#---2d check out the columns in your data set

    analysisDf.columns
    analysisDf.columns.tolist() #how about we make that a list

    analysisDf.info() #lets check the data types -- note we loaded everything as text (equivalent to object in python)

#---2e lets look at some descriptive stats

    analysisDf['Example_Column_Name'].value_counts()  #how many unique objects are in the column 'Example_Column_Name?
    analysisDf['Example_Column_Name'].isnull().value_counts() # are there any null values here? False == not null

#---2f lets look at the kitchen sink

    analysisDf.describe() # by default it will conduct descriptive stats for numerical datatypes the dataset

#--- 2d lets add another column, why not?

    analysisDf_20.assign(Test="Test")

#3 Save the file into the 'ProcessedFiles' folder

csvFileSave(analysisDf_20,'example_data_file.csv')

#Congrats! you've just loaded a data file, worked with a data file, and saved a data file!
