"""
This program was used on the Titanic training data (train.csv).

I split the training dataset by gender and then handled each subset using 
different criteria. If a certain category of passengers had a survival rate 
of greater than 85%, then all were marked as survived. Similarly, if a certain 
category of passengers had a survival rate of less than 15%, then all were 
marked as perished. For passenger data between 15%-85% survival rate, I 
further split them by other categories. Among these subsets, passengers in 
any group with 50% or higher survival rate were all marked as survived; 
all others were marked as perished. In the end the following criteria was 
used for determining survival:

1. All 1st and 2nd class female passengers
2. All 3rd class female children and teenagers (less than 20 years)
3. All male children (less than 10 years)

Anyone not in the above three criteria was marked as perished.
"""
#-----------------------------------------------------------------------------#
import csv
import numpy as np

#-----------------------------------------------------------------------------#

training_file = csv.reader(open('train.csv', 'rb'))
header = training_file.next()

data = []
for row in training_file:
    if row[4] == '':  # row[4] is age
        if 'Mrs' in row[2] or 'Mr' in row[2]:
            row[4] = 100
        else:
            row[4] = 0

    data.append(row)

data = np.array(data)

#-----------------------------------------------------------------------------#

x = "| %.0f" # Format variable
print '\nTotal Passengers:', len(data)
print 'Passenger Type | Total | No. Survived | % Survived'

#-----------------------------------------------------------------------------#
"""
All male and all female data
"""

w = data[data[0::,3] == "female"]
temp = np.sum(w[0::,0].astype(np.float))
print 'All Women |', len(w), x % temp, x % (temp/len(w) * 100)

m = data[data[0::,3] != "female"]
temp = np.sum(m[0::,0].astype(np.float))
print 'All Men |', len(m), x % temp, x % (temp/len(m) * 100)

#-----------------------------------------------------------------------------#
"""
1st, 2nd, and 3rd class female data
"""

fc_w = data[(data[0::,3] == "female") & (data[0::,1] == '1')]
temp = np.sum(fc_w[0::,0].astype(np.float))
print '1st Class Women |', len(fc_w), x % temp, x % (temp/len(fc_w) * 100)

sc_w = data[(data[0::,3] == "female") & (data[0::,1] == '2')]
temp = np.sum(sc_w[0::,0].astype(np.float))
print '2nd Class Women |', len(sc_w), x % temp, x % (temp/len(sc_w) * 100)

tc_w = data[(data[0::,3] == "female") & (data[0::,1] == '3')]
temp = np.sum(tc_w[0::,0].astype(np.float))
print '3rd Class Women |', len(tc_w), x % temp, x % (temp/len(tc_w) * 100)

#-----------------------------------------------------------------------------#
"""
3rd class female adult and child data
"""

ch_tc_w = data[(data[0::,3] == "female") & (data[0::,1] == '3') & (data[0::,4].astype(np.float) < 20)]
temp = np.sum(ch_tc_w[0::,0].astype(np.float))
print '3rd Class Women Child |', len(ch_tc_w), x % temp, x % (temp/len(ch_tc_w) * 100)

ad_tc_w = data[(data[0::,3] == "female") & (data[0::,1] == '3') & (data[0::,4].astype(np.float) >= 20)]
temp = np.sum(ad_tc_w[0::,0].astype(np.float))
print '3rd Class Women Adult |', len(ad_tc_w), x % temp, x % (temp/len(ad_tc_w) * 100)

#-----------------------------------------------------------------------------#
"""
1st, 2nd, and 3rd class male data
"""

fc_m = data[(data[0::,3] != "female") & (data[0::,1] == '1')]
temp = np.sum(fc_m[0::,0].astype(np.float))
print '1st Class Men |', len(fc_m), x % temp, x % (temp/len(fc_m) * 100)

sc_m = data[(data[0::,3] != "female") & (data[0::,1] == '2')]
temp = np.sum(sc_m[0::,0].astype(np.float))
print '2nd Class Men |', len(sc_m), x % temp, x % (temp/len(sc_m) * 100)

tc_m = data[(data[0::,3] != "female") & (data[0::,1] == '3')]
temp = np.sum(tc_m[0::,0].astype(np.float))
print '3rd Class Men |', len(tc_m), x % temp, x % (temp/len(tc_m) * 100)

#-----------------------------------------------------------------------------#
"""
All male adult and child data
"""

ch_m = data[(data[0::,3] != "female") & (data[0::,4].astype(np.float) < 10)]
temp = np.sum(ch_m[0::,0].astype(np.float))
print 'All Male Child |', len(ch_m), x % temp, x % (temp/len(ch_m) * 100)

ad_m = data[(data[0::,3] != "female") & (data[0::,4].astype(np.float) >= 10)]
temp = np.sum(ad_m[0::,0].astype(np.float))
print 'All Male Adult |', len(ad_m), x % temp, x % (temp/len(ad_m) * 100)

#-----------------------------------------------------------------------------#
