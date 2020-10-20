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
hormonename = []
hormoneabb = []

with open('hormonetable.txt', 'r') as file:
    file.readline()
    for line in file:
        line = line.strip().split()
        hormonename.append(line[0])
        hormoneabb.append(line[-1])
file.close()

dataformat = ("INSERT INTO HormonesAssociatedwSyndromeX"
              "(Hormone_Name, Abbreviation)"
              "VALUES (%s, %s)")

for i in range(0, len(hormonename)-1):
    countData = ((hormonename[i]), (hormoneabb[i]))
    cursor.execute(dataformat,countData)

cnx.commit()
