import re
import os
import glob

"""
  This code cleans out the special charecters using the regular expressions.

"""



datapath="/Users/eklavya/WORK_RAJ/BOOTH/Measuring-Corporate-Culture-Using-Machine-Learning/data_booth/DEFC14A/"

def cleanData(doc):
    TAG_RE = re.compile(r"[@, ., \-, ?, :,(, ),\[, \], \/, \%,\\,\', \$,\&, \
                           \`, \>, \*,\=,\+, \_, ;, \", \", #, \!,>,<, ^0-9]")
    return TAG_RE.sub(' ', doc)
    
    


def readFile(filename):
    data=[]
    with open(filename, "r") as f:
        indata = f.readlines()
    
    for i in range(len(indata)):
        data.append(indata[i].rstrip())  
    return data
        


def readDataSet(datapath):
    dataSet=[]
    
    for filename in glob.glob(datapath+'*.txt'):
        dataSet.append(readFile(filename))
    
    return dataSet



def processData(data):
    cData=[]
    for i in range(len(data)):
        for j in range(len(data[i])):
            cData.append((cleanData(data[i][j])).strip())
    return cData



if __name__ == "__main__":
    if not os.path.exists('clean_data'):
        os.makedirs('clean_data')

    output_path=''.join("/Users/eklavya/WORK_RAJ/BOOTH/Measuring-Corporate-Culture-Using-Machine-Learning/data_booth/clean_data/")
    
    filename = os.path.join(output_path,"clean_data.txt" )
    data=readDataSet(datapath)
    pData=processData(data)
    parsed_str='\n'.join(pData)
    fh = open(filename, "w")
    fh.writelines(parsed_str)








    
        