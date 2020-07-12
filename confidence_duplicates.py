import csv
import re
from difflib import SequenceMatcher
import operator

TO CLEAN

with open('FilteredOut.csv', 'r') as fin, open ("FilteredOutOut.csv", 'w') as fout:
    reader = csv.reader(fin, delimiter=';')
    writer = csv.writer(fout, delimiter=';')
    confidence = 0.7
    sorted = sorted(reader, key=operator.itemgetter(4), reverse=True) #ordinati per testo
    for i in range(0, len(sorted)):
        line1 = sorted[i]
        print(i)
        if (i+1 >= len(sorted)):
            break
        else:
            line2 = sorted[i+1]
        if (SequenceMatcher(None, line1[4], line2[4]).ratio() < confidence):
            writer.writerow(line1)

TO SORT IT BACK

import csv
from datetime import datetime
with open ("FilteredOutOut.csv", 'r') as fin:
    reader = csv.reader(fin, delimiter=';')
    sorted = sorted(reader, key = lambda row: datetime.strptime(row[1], "%d/%m/%y %H:%M"))
    with open("Final.csv", "w") as f:
        fileWriter = csv.writer(f, delimiter=';')
        for row2 in sorted:
            fileWriter.writerow(row2)
