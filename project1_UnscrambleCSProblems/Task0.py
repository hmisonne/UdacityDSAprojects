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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# the first record will be located on the first line: text[0]
print("First record of texts, {} texts {} at time {}".format(*texts[0]))

# the last record will be located on the last line: calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*calls[-1]))