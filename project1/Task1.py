"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniqueTelNumbers = set()

for line in texts:
    uniqueTelNumbers.update([line[0],line[1]])

for line in calls:
    uniqueTelNumbers.update([line[0],line[1]])
count= len(uniqueTelNumbers)

print("There are "+str(count)+" different telephone numbers in the records.")
