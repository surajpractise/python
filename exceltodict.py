import pandas as pd

def exceltodict():
    #importing the data from excel
    newdata = pd.read_excel(r'C:\Users\SURAJ MASTHAN\Desktop\Excel\Book2.xlsx')
    #grouping the data based on columns
    dfgrp = newdata.groupby(['Jira_ID','Component_Type','CCN','Revision'])
    completeList = []
    #Adding the complete data to list based on groups
    for name,group in dfgrp:
        completeList.append(group)
    length = len(completeList)
    fcList = []
    individualdict ={}
    tmpList = []
    finalValues =[]
    tmpValues = []
    count = 0
    for i in range(length):
        tmpList = completeList[i]
        individualdict[i] = tmpList.to_dict('records')
        finalValues.append(individualdict[i])
    print(finalValues)
    return finalValues

exceltodict()
