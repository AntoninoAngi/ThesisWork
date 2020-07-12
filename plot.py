# IO

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("new_synonyms.csv", sep=";")
df["year"] = df["date"].apply(lambda x: x.split("/")[2])
df["year"] = df["year"].apply(lambda x: x.split(" ")[0])
df["year"] = "20" + df["year"]
df["month"] = df["date"].apply(lambda x: x.split("/")[1])
df.groupby([df["year"], df["month"]]).count().plot(kind="bar", legend=None)
plt.show()
