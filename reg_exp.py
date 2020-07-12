
#filter texts that only contained urls, hashtags or mentions

import csv
import re
i = 0
c = 0
with open('Filtered.csv', 'r') as fin, open ("FilteredOut.csv", 'w') as fout:
    reader = csv.reader(fin, delimiter=';')
    writer = csv.writer(fout, delimiter=';')
    for row in reader:
        i = i+1
        contains_url = re.split('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', row[4])
        only_hashtags = re.split('^\s*(?:#\w+\s*)+$', row[4])
        only_mentions = re.split('^\s*(?:@\w+\s*)+$', row[4])
        x = row[4].replace(row[5], "") #text - mentions
        y = x.replace(row[6], "") #text - hashtag
        #if numero degli spazi del testo rimanente > 10 allora controllare altrimenti niente
        if (y.count(" ") > 10):
            writer.writerow(row)
        else:
            c = c + 1
print(c)
