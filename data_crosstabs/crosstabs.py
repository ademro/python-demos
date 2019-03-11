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
pd.set_option('display.max_columns',100)
#Sets directory path of the .py file
curDir=os.getcwd()
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

#load an Excel File -- note the variable headerLoc denotes the row that should be used for your dataframe labels and the variable sheetName denotes the excel sheet you want to load into a dataframe
def loadExcelfile(excelFile,headerLoc,sheetName):
    df=pd.DataFrame(pd.read_excel(os.path.join(curDir,feedFileLocation+excelFile),header=headerLoc,dtype=str,sheet_name=sheetName))
    return df

#save a dataframe to CSV
def csvFileSave(arrayName,fileName):
    table=DataFrame(arrayName)
    table.to_csv(os.path.join(curDir,processedFileLocation+fileName),index=False,sep=',')

#Step 1 ---- Load the Data into a DataFrame

analysisDf = loadCSVfile('adult.csv')

#Step 2 ---- Examine the Data

#Examine column datatypes -- you should see they are all text (object)

analysisDf.dtypes

#Examine the dataframe columns to see if any dtype adjustments are required.  It looks like age, capital-gain, capital-loss, and hours-per should have numeric dtypes

analysisDf.columns.tolist()

#Examine the numeric columns to confirm they are indeed numeric instead of categorical.  Because you can see a wide variation in numerical variables by row, this does indicate the variables are numeric rather than binary or categorical.

analysisDf.loc[50:60,('age','capital-gain','capital-loss','hours-per')]

#Step 3 ---- Set the age, capital-gain, capital-loss, hours-per to a integer data type

analysisDf[['age','capital-gain','capital-loss','hours-per']]=analysisDf[['age','capital-gain','capital-loss','hours-per']].astype(dtype='int')
analysisDf.dtypes

# Step 4 ---- Use crosstabs to better understand your data.  Say you wanted to better understand the education distribution by race within the data set.  To accomplish this you could create a crosstab with the education classification as a row with the race as the column header.  This operation first identifies the number of samples with a given education then calculates tne number of samples within that education classification belonging to a particular race.

pd.crosstab(analysisDf['education'],columns=analysisDf['race'])

#It is great that we have the raw sample size beloging to the education and race categories.  What this does not tell you is the proportion of a particular race with a certain level of education.  Do do this you can utilize the 'normalize' parameter.  With this parameter you can identify if you want the crosstab to calculate percentage of a particular category present (by column or row).  Note that in this exampleI multipled the dataframe by 100 to return a percentage.

pd.crosstab(analysisDf['education'],columns=analysisDf['race'],normalize='columns')*100

#Now the data is in a useful form in which you can draw comparative conclusions

#Say now you wated to understand the average number of hours worked per week by segment.  Because we changed the variable 'hours-per' to a numerical data type we can easily do this using a combination of the values and aggfunc parameters.

pd.crosstab(analysisDf['education'],columns=analysisDf['race'],values=analysisDf['hours-per'],aggfunc='mean')
