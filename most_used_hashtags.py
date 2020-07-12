#IO

from collections import Counter
import pandas as pd

df = pd.read_csv("new_synonyms.csv", sep=";")
df["hashtags"] = df["hashtags"].astype(str)
print(Counter(" ".join(df["hashtags"]).split()).most_common(30))
