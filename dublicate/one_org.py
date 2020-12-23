import pandas as pd
import functions as fun

file_trud = 'data/ut.csv'
file_addr = 'data/ua.csv'

df = pd.read_csv(file_trud, sep=";")
dfa = pd.read_csv(file_addr, sep=",")

df_gt = df.groupby("tn")
df_ga = dfa.groupby("tn")


tt_tn, nums_trud = fun.filter_tn(df_gt)
ta_tn, nums_addr = fun.filter_tn(df_ga)

data_trud = {"Табельный номер": tt_tn, "Количество ошибок": nums_trud}
data_addr = {"Табельный номер": tt_tn, "Количество ошибок": nums_trud}

df_t = pd.DataFrame(data_trud)
df_a = pd.DataFrame(data_addr)
print(df_a)
df_t.to_csv("data/err_trud.csv", sep=";", decimal=",")
df_t.to_csv("data/err_addr.csv", sep=";", decimal=",")
