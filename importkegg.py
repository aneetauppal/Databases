
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
uniprotid = []
keggid = []
genes = []

with open('keggsdata2.csv', 'r') as file:
    file.readline()
    for line in file:
        line = line.strip().split(',')
        uniprotid.append(line[0])
        keggid.append(line[1])
        genes.append(line[2])
file.close()

dataformat = ("INSERT INTO Pathwayinformation"
              "(UniPro_ID, Kegg_ID, Genes_involved)"
              "VALUES (%s, %s, %s)")

for i in range(0, len(uniprotid)-1):
    countData = ((uniprotid[i]), (keggid[i]), (genes[i]))
    cursor.execute(dataformat,countData)

cnx.commit()
