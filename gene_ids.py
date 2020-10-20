#!/usr/bin/python

import mysql.connector 

config = {
  'user': '',
  'password': '',
  'host': '',
  'database':'',
  'raise_on_warnings': True,
}

# open the connection                                                                                                                                       
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# Make database connection
geneid = []
name = []

with open('allgenesforsynx.txt', 'r') as file:
    file.readline()
    for line in file:
        line = line.strip().split()
        geneid.append(line[0])
        name.append(line[1])
file.close()

dataformat = ("INSERT INTO GenesAssociatedwSyndromeX"
              "(Gene_ID, Gene_Name)"
              "VALUES (%s, %s)")

for i in range(0, len(geneid)-1):
    countData = ((geneid[i]), (name[i]))
    cursor.execute(dataformat,countData)

cnx.commit()
