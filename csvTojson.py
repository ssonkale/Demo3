# importing the required libraries
import csv
import json


# defining the function to convert CSV file to JSON file
def convjson(csvFilename, jsonFilename):
    # creating a dictionary
    mydata = {}

    # reading the data from CSV file
    with open(csvFilename,'r') as csvfile:
        csvRead = csv.DictReader(csvfile)

        # Converting rows into dictionary and adding it to data
        for rows in csvRead:
            mykey = rows['ID']
            mydata[mykey] = rows

            # dumping the data
    with open(jsonFilename, 'w') as jsonfile:
        jsonfile.write(json.dumps(mydata, indent=4))

    # filenames


with open("student.csv","w",newline='') as fp:
    writer= csv.writer(fp)

    writer.writerow(['ID','Name','Address','Contact'])
    writer.writerow([1,'Tushar','Pune',999000099])
    writer.writerow([2,'Piyu','Pune',999000100])
    writer.writerow([3,'Sandhya','Pune',999055778])

    info=[[4,'Trisha','Pune',999000099],[5,'Priya','Pune',999000099],[6,'Shivam','Pune',999000099]]

    writer.writerows(info)

csvFilename = r'student.csv'
jsonFilename = r'jsonfile.json'


# Calling the convjson function
convjson(csvFilename, jsonFilename)