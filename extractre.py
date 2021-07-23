import re
sampleValue = 'OT'
leftSpace = '(\S+) '
rightSpace = ' (\S+)'
leftValue = leftSpace+sampleValue
rightValue = sampleValue+rightSpace
finalValue= ""

def extractmatchvalues(orderval):

    with open(r'SamplePDFTxtFile.txt') as f:
        for line in f:
            match = re.search(orderval, line)
            if match:
                finalValue = match.group(1)
                #print('final value:', finalValue)
                return finalValue


extractmatchvalues(leftValue)