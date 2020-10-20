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
id = []
drugname = []
protein = []
function = []

with open('druginfo.csv', 'r') as file:
    file.readline()
    for line in file:
        line = line.strip().split(',')
        drugname.append(line[0])
        protein.append(line[1])
        function.append(line[2])
        id.append(line[-1])

file.close()

dataformat = ("INSERT INTO DrugsAssociatedwDiseases"
              "(Drug_ID, Drug_Name, Protein_affected, Functionality)"
              "VALUES (%s, %s, %s, %s)")

for i in range(0, len(id)-1):
    countData = ((id[i]), (drugname[i]), (protein[i]), (function[i]))
    cursor.execute(dataformat,countData)

cnx.commit()
