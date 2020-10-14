import pandas as pd

df = pd.read_csv("nadym.csv", sep=";")
df["key"] = range(1, 615)
print(df.info)
df.set_index("key", inplace=True)
print(df.iloc(0))