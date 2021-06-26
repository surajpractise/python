import pandas as pd
import json
import functools
import datetime
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
y= fileDir.replace('\Library','')
filepath = os.path.join(y, 'C:\\Users\\SURAJ MASTHAN\\Desktop\\Excel\\Book2.xlsx')

def ExtractExceltoFormat():
    #importing the data from excel
    newdata = pd.read_excel(filepath,sheet_name='Phase In Phase Out')
    #grouping the data based on columns
    dfgrp = newdata.groupby(['Jira_ID','Component_Type','CCN','New Revision'])
    completeList = []
    #Adding the complete data to list based on groups
    for name,group in dfgrp:
        completeList.append(group)
    length = len(completeList)
    individualdict ={}
    tmpList = []
    finalValues =[]
    individualList=[]
    extractedListValues=[]
    startDate =""
    endDate = ""

    for i in range(length):
        tmpList = completeList[i]
        individualdict[i] = tmpList.to_dict('records')
        individualList = individualdict[i]
        for j in range(len(individualList)):
            startDateInput = individualList[j]["Start Date"]
            effectiveDateInput = individualList[j]["Effective Date"]
            startDateFormat = startDateInput.strftime('%d-%m-%y')
            effectiveDateFormat = effectiveDateInput.strftime('%d-%m-%y')
            individualList[j]["Start Date"] = startDateFormat
            individualList[j]["Effective Date"] = effectiveDateFormat

        extractedListValues.extend(individualList)
    finalValues = json.dumps(extractedListValues)
    return finalValues, length
ExtractExceltoFormat()
