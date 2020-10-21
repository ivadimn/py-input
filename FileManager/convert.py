import pandas as pd

fpath = "/home/vadim/"
file_trud = "trud1.csv"

with open(f"{fpath}{file_trud}", "r", encoding="cp1251") as ft:
    content = ft.read(200)

#lines = content.decode(encoding="cp1251")
print(content)

#with open(f"{fpath}test1.csv", "w", encoding="utf-8") as ft1:
#    ft1.writelines(lines)"""

#df = pd.read_csv(f"{fpath}{file_trud}", sep=";")
#print(df.head())