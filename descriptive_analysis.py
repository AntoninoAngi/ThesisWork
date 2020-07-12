
# IO

import pandas as pd
df = pd.read_csv('new_synonyms.csv', sep=";")
df = df.sort_values('favorites')
df.tail(20).to_csv("prova.csv", index=False, sep=";")