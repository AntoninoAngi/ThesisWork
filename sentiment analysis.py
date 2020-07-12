#sentiment analysis

from textblob import TextBlob
import csv

neu = 0
pos = 0
neg = 0
with open('new_synonyms.csv', 'r') as fin, open('Sent_Analysis.csv', 'w') as fout:
    writer = csv.writer(fout, delimiter=';')
    for row in csv.reader(fin, delimiter=';'):
        obj2 = row[4]
        obj = TextBlob(obj2)
        sentiment = obj.sentiment.polarity
        if sentiment == 0:
            row.append('neutral')
            neu += 1
        elif sentiment > 0:
            row.append('positive')
            pos += 1
        else:
            row.append('negative')
            neg += 1
        writer.writerow(row)

print("Neutral: " + str(neu))
print("Positive: " + str(pos))
print("Negative: " + str(neg))
