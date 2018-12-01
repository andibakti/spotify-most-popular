import os 
import csv
import utils

data_dir = 'viral/data/'
filtered_dir = 'viral/filtered/'

def filterdata():
    for filename in os.listdir(data_dir):
        utils.currentFile(filename)
        file = open(data_dir + filename, 'r+')
        out = open(filtered_dir + filename, 'w+')
        line = file.readline()
        seen = False
        for s in line :
            if s == "\\" :
                seen = True
            elif seen == True and s == "n":
                temp = ',' + filename[:-4]
                out.write(temp + '\n')
                seen = False
            elif seen == True:
                out.write("\\" + s)
                seen = False
            else:
                out.write(s)


        file.close()
        out.close()

def assembledata():
    out = open('viral/results.csv', 'w+')
    for filename in os.listdir(filtered_dir):
        utils.currentFile(filename)
        file = open(filtered_dir + filename, 'r+')
        for line in file:
            if str(line[0]).isdigit:
                out.write(line)
        # with file as csvfile:
        #     reader = csv.reader(csvfile, delimiter=',')
        #     for i, line in enumerate(reader):
        #         if i == 0:
        #             continue
        #         else:
        #             s =  line[]
    out.close()


def filterfile(filename):
    file = open(filename, 'r+')
    out = open('results2.csv', 'w+')
    for line in file.readlines():
        for s in line :
            if s == "^" :
                out.write('\n')
            else:
                out.write(s)
    file.close()
    out.close()
    
filterdata()
assembledata()
#filterfile('results.csv')