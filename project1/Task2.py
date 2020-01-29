"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


# Initialize dictionnary with record of time spent by phone number
recordTimeSpent = {}

for row in calls:
    recordTimeSpent[row[0]]=recordTimeSpent.get(row[0],0) + int(row[3])
    recordTimeSpent[row[1]]=recordTimeSpent.get(row[1],0) + int(row[3])

# Iterate over values of dictonnary to find the number that spent the longest time on the phone.
longestTime = 0
for key, value in recordTimeSpent.items():
#     Initialize longestTime with first record
    if longestTime == 0:
        telephoneNumber = key
        longestTime = value
    elif longestTime < value:
        telephoneNumber = key
        longestTime = value

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephoneNumber,longestTime))



