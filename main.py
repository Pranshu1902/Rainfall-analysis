# Rainfall analysis and comparision in different districts

import numpy as np
import pandas as pd

df = pd.read_csv("district wise rainfall normal.csv")

name = []
val = []

for i in range(len(df.iloc[0:,0])):
    main = df.iloc[i, 2:14]
    val.append([main.mean(), main.std(), main.min(), main.max()])
    name.append(df.iloc[i,1])
new = pd.DataFrame(val, index=name, columns=["mean", "std", "min", "max"])
print(new)
