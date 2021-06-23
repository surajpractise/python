import pandas as pd
import json
import functools

def ExtractExceltoFormat():
    #importing the data from excel
    newdata = pd.read_excel(r'C:\Users\SURAJ MASTHAN\Desktop\Excel\Book3.xlsx')
    #grouping the data based on columns
    dfgrp = newdata.groupby(['Jira_ID','Component_Type','CCN','Revision'])
    completeList = []
    #Adding the complete data to list based on groups
    for name,group in dfgrp:
        completeList.append(group)
    length = len(completeList)

    individualdict ={}
    tmpList = []
    finalValues =[]
    tmpValues = []
    countryCode=[]
    countryName=[]
    individualList=[]
    combinedCntryCode =""
    combinedCntryName =""
    modifiedListValues=[]
    extractedListValues=[]

    for i in range(length):
        tmpList = completeList[i]
        individualdict[i] = tmpList.to_dict('records')
        individualList = individualdict[i]
        for j in range(len(individualList)):
            countryCode.append(individualList[j]["Coutry_Code"])
            countryName.append(individualList[j]["Product_Country"])
        combinedCntryCode = functools.reduce(lambda a,b: a+","+b,countryCode)
        combinedCntryName = functools.reduce(lambda a,b: a+","+b,countryName)
        countryCode=[]
        countryName=[]

        modifiedListValues = individualdict[i][0]
        del modifiedListValues['Coutry_Code']
        del modifiedListValues['Product_Country']
        modifiedListValues['Coutry_Code'] = combinedCntryCode
        modifiedListValues['Product_Country'] = combinedCntryName

        extractedListValues.append(modifiedListValues)
    finalValues = json.dumps(extractedListValues)
    #print(finalValues)
    return finalValues
ExtractExceltoFormat()
