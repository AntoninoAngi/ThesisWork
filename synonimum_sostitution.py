
import csv
from nltk.corpus import wordnet as wn

with open('data_processed.csv', 'r') as fin:
    reader = csv.reader(fin, delimiter=';')
    with open('new_synonyms.csv', 'w') as fout:
        writer = csv.writer(fout, delimiter=';')
        for row in reader:
            word = ""
            for i in row[12].split():
                possible_senses = wn.synsets(i)
                if possible_senses and i != "prep":
                    try:
                        x = possible_senses[1].lemma_names()
                        modified_sentence = x[0]
                    except:
                        x = possible_senses[0].lemma_names()
                        modified_sentence = x[0]
                else:
                    modified_sentence = i
                word += " " + modified_sentence
                print(word)

            row.append(word)
            writer.writerow(row)
