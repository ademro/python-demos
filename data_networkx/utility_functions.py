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

#load an Excel File -- note the variable headerLoc denotes the row that should be used for your dataframe labels and the variable sheetName denotes the excel sheet you want to load into a dataframe
def loadExcelfile(excelFile,headerLoc,sheetName):
    df=pd.DataFrame(pd.read_excel(os.path.join(curDir,feedFileLocation+excelFile),header=headerLoc,dtype=str,sheet_name=sheetName))
    return df

#save a dataframe to CSV
def csvFileSave(arrayName,fileName):
    table=DataFrame(arrayName)
    table.to_csv(os.path.join(curDir,processedFileLocation+fileName),index=False,sep=',')