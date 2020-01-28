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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
telemarkNumbers = set()
regularNumbers = set()

# Identify numbers that send or receive texts and add to regularNumbers list
for line in texts:
    if line[0] not in regularNumbers:
        regularNumbers.add(line[0])
    elif line[1] not in regularNumbers:
        regularNumbers.add(line[1])
# Identify numbers that make receive incoming calls and add to regularNumbers list
for line in calls:
    if line[1] not in regularNumbers:
        regularNumbers.add(line[1])

# Identify numbers that make outgoing calls which are not in the regularNumbers list
for line in calls:
    if line[0] not in regularNumbers:
        telemarkNumbers.add(line[0])


print("These numbers could be telemarketers: ")
for number in sorted(telemarkNumbers):
    print(number)
    
