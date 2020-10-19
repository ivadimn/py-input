import pandas as pd

file_trud = "/home/vadim/trud.csv"
orgs = {
    'ООО "Газпром добывча Астрахань"' : 'Газпром добыча Астрахань',
    'ООО "Газпром добывча Иркутск"' : 'Газпром добыча Иркутск',
    'ООО "Газпром добывча Краснодар"' : 'Газпром добыча Краснодар',
    'ООО "Газпром добывча Надым"' : 'Газпром добыча Надым',
    'ООО "Газпром добывча Ноябрьск"' : 'Газпром добыча Ноябрьск',
    'ООО "Газпром добывча Уренгой"' : 'Газпром добыча Уренгой',
    'ООО "Газпром добывча Ямбург"' : 'Газпром добыча Ямбург',
    'OOO "Газпром трансгаз Волгоград"': 'Газпром трангаз Волгоград',
    'OOO "Газпром трансгаз Екатеринбург"': 'ГП трансгаз Екатеринбург',
    'OOO "Газпром трансгаз Москва"': 'Газпром трансгаз Москва',
    'OOO "Газпром трансгаз Нижний Новгород"': 'Газпром тргаз Н Новгород',
    'OOO "Газпром трансгаз Самара"': 'Газпром трансгаз Самара',
    'OOO "Газпром трансгаз Саратов"': 'Газпром трансгаз Саратов',
    'OOO "Газпром трансгаз Сургут"': 'Газпром трансгаз Сургут',
    'OOO "Газпром трансгаз Томск"': 'Газпром трансгаз Томск',
    'OOO "Газпром трансгаз Уфа"': 'Газпром трансгаз Уфа',
    'OOO "Газпром трансгаз Ухта"': 'Газпром трансгаз Ухта',
    'OOO "Газпром трансгаз Чайковский"': 'Газпром тр.газ Чайковский',
    'OOO "Газпром трансгаз Югорск"': 'Газпром трансгаз Югорск',
    'OOO "Газпром ПХГ"': 'Газпром ПХГ',
    'OOO "Газпром переработка"' : 'Газпром переработка'
}
def filter_groups_trud(groups):
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

df = pd.read_csv(file_trud, sep=";")
print(df.head())
"""for org_name,file_name in orgs.items():
   df_org = 
   df_group = df.groupby("tn")
   org_names.append(org_name)
   total_counts.append(len(df))
   tn_list, count_list = filter_groups_trud(df_group)
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
print(df_tn)"""