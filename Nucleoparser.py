#!/usr/bin/python

GeneID = []
Gene_seq = []

with open ('/Users/aneetauppal/Downloads/biopython-95c5fa63221d03a9f84f653fa2039fec90b72de9/gene_nucleo_seq/gene_seq_all.txt', 'r') as file:
    # file.readline()
     for line in file:
         # line = line.strip().split()
          if line.startswith('Homo'):
               line = line.strip().split()
  #GeneID.append(line[0])
               Gene_seq.append(line[0])
               print line
     print Gene_seq 
          
               
          #print (Gene_seq[-1], Gene_seq[0])
          
