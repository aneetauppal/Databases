#!/usr/bin/python

import urllib

file = open('/Users/aneetauppal/CHS/Database/Data/Txt_mining_files/Scripts/DMpubmedid17.txt', 'r')
for line in file:
    lines = line.strip()
    code = str(lines)
    data = urllib.urlopen("http://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/Gene/" + code + "/PubTator/").read()
    print data
