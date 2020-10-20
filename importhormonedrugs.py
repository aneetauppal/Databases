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
drugid = []
drugname = []
hormone = []

with open('hormonedrugs.csv', 'r') as file:
    file.readline()
    for line in file:
        line = line.strip().split(',')
        drugid.append(line[0])
        drugname.append(line[1])
        hormone.append(line[2])
file.close()

dataformat = ("INSERT INTO DrugsAssociatedwithHormones"
              "(Drug_ID, Drug_Name, Hormone_Name)"
              "VALUES (%s, %s, %s)")

for i in range(0, len(drugid)-1):
    countData = ((drugid[i]), (drugname[i]), (hormone[i]))
    cursor.execute(dataformat,countData)

cnx.commit()
