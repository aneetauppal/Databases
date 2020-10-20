#!/usr/bin/python

Gene_ID = []
Gene_symbol = []
with open('/Users/aneetauppal/Downloads/geneIDSandSym.txt', 'r') as file:
    file.readline()
    for line in file:
        line = line.strip().split('\t')
        Gene_ID.append(line[0])
        Gene_symbol.append(line[1])

       

        for i in range (0,len(Gene_ID)-1):
            print (Gene_ID[i], (str(Gene_symbol[i]))) 
