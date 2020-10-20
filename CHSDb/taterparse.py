#!/usr/bin/python

import sets

with open('/Users/aneetauppal/CHS/Database/Data/Txt_mining_files/DryMouth/DM_genes_unparsed/DMgenesbatch1_18unparsed.txt') as infile:
    dictionary = {}
    for line in infile:
        if "|a|" not in line:
            if "|t|" not in line:
                    #print line
                linesstrip = line.strip()
                linessplit = line.split()
                try:
                    #dictionary[(linessptrip[0])] = (linessptrip[-1])
                     lists = [linessplit[0], linessplit[-1]]
                     print lists
                     #print dictionary
                except IndexError:
                    pass


            #print(line.split()[:6])
