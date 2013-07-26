"""
This program was used on the Titanic testing data (test.csv). Output was 
stored in titanic_test.csv. Mark '0' for deceased person and '1' for survived

Following criteria was used for determining survival:
1. All 1st and 2nd class female passengers
2. All 3rd class female children and teenagers (less than 20 years)
3. All male children (less than 10 years)
See titanic_train.py for more details.

Some of the passengers were missing the age attribute, but all the passengers 
had salutations in their name attribute. Any passenger that had 'Mr' or 'Mrs' 
in their name was marked as adult; all others were marked as children 
(Master, Miss).
"""

#-----------------------------------------------------------------------------#
import csv
import numpy as np

#-----------------------------------------------------------------------------#
testing_file = csv.reader(open('test.csv', 'rb'))
header = testing_file.next()
out_file = csv.writer(open("titanic_test.csv", "wb"))


c1, c2, c3, c4 = 0, 0, 0, 0

for row in testing_file:

    if row[3] == "":
        if 'Mrs' in row[1] or 'Mr' in row[1]:
            row[3] = 100
        else:
            row[3] = 0

    if row[2] == "female" and row[0] in ['1', '2']:
        row.insert(0,'1')
        c1 += 1
    
    elif row[2] == "female" and row[0] == '3' and float(row[3]) < 20:
        row.insert(0,'1')
        c2 += 1
    
    elif row[2] == "male" and float(row[3]) < 10:
        row.insert(0,'1')
        c3 += 1

    else:
        row.insert(0,'0')
        c4 += 1
    
    out_file.writerow(row)

#-----------------------------------------------------------------------------#
print "Total Passengers: " + str(c1+c2+c3+c4)
print "Total Survived: " + str(c1+c2+c3)
print "Female 1st and 2nd Class: " + str(c1)
print "Female 3rd Class under 20: " + str(c2)
print "Male under 10: " + str(c3)
print "Total Perished: " + str(c4)
print "\nThe output was stored in titanic_test.csv\n"

#-----------------------------------------------------------------------------#
