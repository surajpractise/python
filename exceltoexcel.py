import pandas as pd
import functools
#importing the data from excel
newdata = pd.read_excel(r'C:\Users\SURAJ MASTHAN\Desktop\Excel\Book1.xlsx')
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

listValues=[]
individualList =[]
countryName =[]
countryCode =[]
combinedCntryName = ""
modListValues = {}
extractedListValues=[]
extractedDictValues = {}
for i in range(length):
    tmpList = completeList[i]
    individualdict[i] = tmpList.to_dict('records')
    finalValues.append(individualdict[i])

lenFinalValues = len(finalValues)
for j in range(lenFinalValues):
    listValues=finalValues[j]
    print("listValues:",listValues)

    lenListValues = len(listValues)

    #print("lenListValues:",lenListValues)
    for k in range(lenListValues):
        individualList=listValues[k]
        #countryName.append(individualList["Product_Country"])
        countryCode.append(individualList["Coutry_Code"])
        countryName.append(individualList["Product_Country"])
        #print("individualList:",individualList)
    #print("countryName:",countryName)
    combinedCntryCode = functools.reduce(lambda a,b: a+"|"+b,countryCode)
    combinedCntryName = functools.reduce(lambda a,b: a+"|"+b,countryName)
    #combinedCntryValues ='"'+"{'CountryCodeName'"+":"+ combinedCntryCode+","+combinedCntryName+"}"+'"'
    combinedCntryValues =combinedCntryCode+","+combinedCntryName
    print("functools:",combinedCntryValues)

    countryCode=[]
    countryName=[]
    print("count of j:",j)
    print("Inside Error:",listValues[j])
    modListValues = listValues[j]

    del modListValues['Coutry_Code']
    del modListValues['Product_Country']
    modListValues['CountryCodeName'] = combinedCntryValues
    extractedListValues.append(modListValues)
    print("modListValues:",type(modListValues))

print("extractedListValues:",extractedListValues)
df = pd.DataFrame(extractedListValues)
df = df.set_index("Jira_ID")
print("df values:",df)
df.to_excel("output.xlsx")





#countryName = listValues[0]["Product_Country"]
#countryName1 = listValues[1]["Product_Country"]
#combinedCntryName = countryName+"|"+countryName1
#print(combinedCntryName)
#dictValues = finalValues[0][0]
#print("dictValues:",dictValues)
#df = pd.DataFrame(data=dictValues,index=[0])
#print("df values:",df)
#df.to_excel("output.xlsx")
#print(type(finalValues[0][0]))
