import pandas as pd
import os

fpath = '/home/vadim/errors.csv'
fpath_convert = '/home/vadim/errors1.csv'
file_trud = ""

print("started")
fc = open(fpath_convert, "wb")
with open(fpath, "rb") as ft:
    for content in ft:
        convert = content.decode(encoding="UTF-8")
        fc.write(convert.encode(encoding="cp1251"))
fc.flush()
fc.close()
print("finished")

#lines = content.decode(encoding="cp1251")
#for dirpath,dirname,filename in os.walk(fpath):
#    print(dirpath,dirname,filename)

#with open(f"{fpath}test1.csv", "w", encoding="utf-8") as ft1:
#    ft1.writelines(lines)

#df = pd.read_csv(f"{fpath}{file_trud}", sep=";")
#print(df.head())