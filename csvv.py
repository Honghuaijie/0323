import csv

def readData():
    lt=[]

    with open("testdata.csv",'r',encoding='gbk') as fp:
        reader=  csv.reader(fp)
        next(reader)

        for i in reader:
            lt.append(i)


    return lt

