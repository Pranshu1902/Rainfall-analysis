import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd

plt.style.use('fivethirtyeight')

df = pd.read_csv("district wise rainfall normal.csv")

nicobar = df.iloc[0,2:14]

name = []
val = []

for i in range(len(df.iloc[0:,0])):
    main = df.iloc[i, 2:14]
    val.append([main.mean()])
    name.append(df.iloc[i,1])
new = pd.DataFrame(val, index=name, columns=["mean"])


fig, ax = plt.subplots(2,1)
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

ax[0].bar(month, nicobar, color="green")
ax[1].boxplot(nicobar)
plt.xlabel("Median")
plt.suptitle("Nicobar")


plt.show()
