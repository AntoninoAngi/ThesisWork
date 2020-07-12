DetectorFactory.seed = 0

with open('out.csv', 'r') as fin, open('FilteredData.csv', 'w') as fout:
    writer = csv.writer(fout, delimiter=';')
    for row in csv.reader(fin, delimiter=';'):
        try:
            if detect(row[4]) == 'en':
                writer.writerow(row)
        except:
            print(row[4])
