import pandas as pd

orgs = {
    'OOO "Газпром трансгаз Волгоград"': 'volgograd_trud.csv',
    'OOO "Газпром трансгаз Екатеринбург"': 'ekat_trud.csv',
    'OOO "Газпром трансгаз Москва"': 'moskva_trud.csv',
    'OOO "Газпром трансгаз Нижний Новгород"': 'nnovgorod_trud.csv',
    'OOO "Газпром трансгаз Самара"': 'samara_trud.csv',
    'OOO "Газпром трансгаз Саратов"': 'saratov_trud.csv',
    'OOO "Газпром трансгаз Сургут"': 'surgut_trud.csv',
    'OOO "Газпром трансгаз Томск"': 'tomsk_trud.csv',
    'OOO "Газпром трансгаз Уфа"': 'ufa_trud.csv',
    'OOO "Газпром трансгаз Ухта"': 'uhta_trud.csv',
    'OOO "Газпром трансгаз Чайковский"': 'chaik_trud.csv',
    'OOO "Газпром трансгаз Югорск"': 'ugorsk_trud.csv',
    'OOO "Газпром трансгаз ПХГ"': 'phg_trud.csv',
    'OOO "Газпром трансгаз переработка"' : 'pererab_trud.csv',
}
def filter_groups(groups):
    print(len(groups))
    tn = []
    count =[]
    for name, group in groups:
        if (len(group) > 1):
            tn.append(name)
            count.append(len(group))
    return tn, count
org_names = []
total_counts = []
error_count = []
persent = []
for org_name,file_name in orgs.items():
   df = pd.read_csv(f"data/{file_name}", sep=";")
   df_group = df.groupby("tn")
   org_names.append(org_name)
   total_counts.append(len(df))
   tn_list, count_list = filter_groups(df_group)
   error_count.append(len(tn_list))
   persent.append((len(tn_list) * 100.0) / len(df))


data = {"Дочернее общество": org_names,
        "Общее количество табельных номиеров": total_counts,
        "Количество табельных номиеров с ошибками": error_count,
        "Процент": persent
        }
#print(org_names)
#print(total_counts)
#print(error_count)
#print(persent)
df_tn = pd.DataFrame(data)
print(df_tn)