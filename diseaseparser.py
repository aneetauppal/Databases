#!/usr/bin/python

import itertools
import sys

my_diseasefile = raw_input('Enter your file name:')

def parse_diseasefile(diseasefile):
    file = open(my_diseasefile, 'r')
   # file_out = open('parseddiseasefile.txt', 'w')
    for line in file: 
        upperline = line.upper()
        upperline2 = (upperline.split()[3:7])
        print(upperline2)





       # file_out.write(upperline)

parse_diseasefile(my_diseasefile)
