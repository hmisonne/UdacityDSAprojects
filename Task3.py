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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# PART A
areaCodes = set()
firstNumberMobile = [7,8,9]
for line in calls:
    callerNumber = line[0]
    if callerNumber[:5] =='(080)':
        receiverNumber = line[1]
#             Check if fixed line
        if receiverNumber[0] == '(':
            receiverAreaCode = receiverNumber[1:].split(')')[0]
        #     Check if mobile line
#         if receiverNumber[0] in firstNumberMobile:
        elif " " in receiverNumber:
            receiverAreaCode = receiverNumber[:4]
#         elif receiverNumber[:3] == 140:
#             receiverAreaCode = 140
        areaCodes.add(receiverAreaCode)

            
print("The numbers called by people in Bangalore have codes:")
for code in sorted(areaCodes):
    print(code)

# PART B
bangalorFixedLine = 0
otherLine = 0

for line in calls:
    callerNumber = line[0]
    if callerNumber[:5] =='(080)':
        receiverNumber = line[1]
        if receiverNumber[:5] =='(080)':
            bangalorFixedLine += 1
        else:
            otherLine +=1
percentage = round(bangalorFixedLine/(bangalorFixedLine+otherLine)*100,2)
print(str(percentage)+" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

