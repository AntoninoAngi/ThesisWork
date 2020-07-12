"""Detects the text's language."""

#IO

import csv
from langdetect import detect
translator = Translator()

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
with open('NewCleanedData.csv', 'r') as fin, open ("Filtered.csv", 'w') as fout:
    reader = csv.reader(fin, delimiter=';')
    writer = csv.writer(fout, delimiter=';')
    seen = set()
    for row in reader:
        if "#RT" not in row[4]: #checks for retweets
            if (row[0] + " " + row[4]) not in seen:  # checks for duplicates
                seen.add(row[0] + " " + row[4])
                try:
                    lang = detect(row[4])
                    if lang == 'en': #check if the tweet is in english
                        writer.writerow(row)
                except:
                    print(row)



