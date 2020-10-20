#!/usr/bin/python

with open('/Users/aneetauppal/CHS/Database/Data/Database_files/GSE51092_2.csv') as infile:
    for line in infile:
        # print line
        lines = line.strip()
        lines1 = lines.split(',')
        if lines1[-1] == '':
            pass
        else:
            print lines1

