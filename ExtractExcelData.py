import pandas as pd

def extractExcelData():
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
    #modifying the data into pairs
    for i in range(length):
        tmpList = completeList[i]
        individualdict[i] = tmpList.to_dict('records')
        tmpdict = individualdict[i]
        lentmpdict = len(tmpdict)
        for j in range(lentmpdict):
            list1 = [(k, v) for k, v in tmpdict[j].items()]
            fcList.extend(list1)
    finalValues = pd.Series(fcList).drop_duplicates().tolist()
    return finalValues

extractExcelData()
