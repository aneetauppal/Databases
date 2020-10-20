#!/usr/bin/python

import mysql.connector

config = {
  'user': '',
  'password': '',
   'host': '',
  'database':'',
  'raise_on_warnings': True,
}

#open the connection
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# Make database connection
taxid = []
orgname = []
geneID =[]
currentID = []
status = []
symbol = []
aliases = []
description = []
maplocation = []
chromosome = []
genomicnucleotide = []
startposition = []
endposition = []
orientation = []
exoncount = []
omim = []

with open('/Users/aneetauppal/CHS/Database/Data/Txt_mining_files/SLE/SLEgeneBatchentrezwnomouse.csv', 'r') as file:
    file.readline()
    for line in file:
        line = line.strip().split(',')
        taxid.append(line[0])
        orgname.append(line[1])
        geneID.append(line[2])
        currentID.append(line[3])
        status.append(line[4])
        symbol.append(line[5])
        aliases.append(str(line[6]))
        description.append(str(line[7]))
        maplocation.append(line[8])
        chromosome.append(line[9])
        genomicnucleotide.append(line[10])
        startposition.append(line[11])
        endposition.append(line[12])
        orientation.append(line[13])
        exoncount.append(line[14])
        omim.append(line[15])
file.close()

dataformat = ("INSERT INTO table2_2_SLE_geneinfo"
              "(Tax_id, Organism_name, Gene_ID, CurrentID, Status, Gene_symbol, Aliases, Gene_description, Map_location, Chromosome, Genomic_nucleotide, Start_position, End_position, Orientation, Exon_count, OMIM)"
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

for i in range(0, len(taxid)-1):
    countData = ((taxid[i]), (orgname[i]), (geneID[i]), (currentID[i]), (status[i]), (symbol[i]), (aliases[i]), (description[i]),
    (maplocation[i]), (chromosome[i]), (genomicnucleotide[i]), (startposition[i]), (endposition[i]), (orientation[i]), (exoncount[i]),
    (omim[i]))
    #print countData
    cursor.execute(dataformat, countData)

cnx.commit()
