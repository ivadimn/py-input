import pandas as pd

file_trud = "/home/vadim/test.csv"

def filter_groups(groups):
    print(len(groups))
    tn = []
    count =[]
    for name, group in groups:
        if (len(group) > 1):
            tn.append(name)
            count.append(len(group))
    return tn, count


df = pd.read_csv("nadym.csv", sep=";")
df_group = df.groupby("tn")
tn_list, count_list = filter_groups(df_group)
data = {"Таб.№": tn_list, "Количество": count_list}
df_tn = pd.DataFrame(data)
print(df_tn)