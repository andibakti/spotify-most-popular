import os 
import csv


def filterdata():
    for filename in os.listdir('./data/'):
        print(filename)
        file = open('data/' + filename, 'r+')
        out = open('filtered/' + filename, 'w+')
        line = file.readline()
        for s in line :
            if s == "^" :
                out.write('\n')
            else:
                out.write(s)
        file.close()
        out.close()

def assembledata():
    out = open('results.csv', 'w+')
    for filename in os.listdir('./filtered/'):
        print(filename)
        file = open('filtered/' + filename, 'r+')
        for line in file:
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
    
#filterdata()
#assembledata()
filterfile('results.csv')