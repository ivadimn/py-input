import pandas as pd

file_trud = 'C:\\github\\trud_convert.csv'
file_addr = 'C:\\github\\addr_convert.csv'
orgs = {
    'ООО "Газпром добывча Астрахань"': 20,
    'ООО "Газпром добывча Иркутск"': 440,
    'ООО "Газпром добывча Краснодар"': 30,
    'ООО "Газпром добывча Надым"': 50,
    'ООО "Газпром добывча Ноябрьск"': 40,
    'ООО "Газпром добывча Уренгой"': 70,
    'ООО "Газпром добывча Ямбург"': 240,
    'OOO "Газпром трансгаз Волгоград"': 90,
    'OOO "Газпром трансгаз Екатеринбург"': 100,
    'OOO "Газпром трансгаз Москва"': 140,
    'OOO "Газпром трансгаз Нижний Новгород"': 150,
    'OOO "Газпром трансгаз Самара"': 160,
    'OOO "Газпром трансгаз Саратов"': 180,
    'OOO "Газпром трансгаз Сургут"': 190,
    'OOO "Газпром трансгаз Томск"': 200,
    'OOO "Газпром трансгаз Уфа"': 210,
    'OOO "Газпром трансгаз Ухта"': 220,
  #  'OOO "Газпром трансгаз Чайковский"': 230,
    'OOO "Газпром трансгаз Югорск"': 260,
    'OOO "Газпром ПХГ"': 250,
    'OOO "Газпром переработка"': 80
}


def filter_groups(groups):
    #print(len(groups))
    tn = []
    count = []
    for name, group in groups:
        if (len(group) > 1):
            tn.append(name)
            count.append(len(group))
    return tn, count


org_names = []
total_trud_counts = []
error_trud_count = []
persent_trud = []
total_addr_counts = []
error_addr_count = []
persent_addr = []

df = pd.read_csv(file_trud, sep=";")
dfa = pd.read_csv(file_addr, sep=";", na_values=0)
dfa['rp'] = dfa['rp'].fillna(0)
dfa['rp'].astype("int64")
print(dfa.dtypes)
for org_name, razdel in orgs.items():
    df_org = df[df.rp == razdel]
    print(f"{org_name} - {len(df_org)}")
    df_group = df_org.groupby("tn")
    org_names.append(org_name)
    total_trud_counts.append(len(df_org))
    tn_list, count_list = filter_groups(df_group)
    error_trud_count.append(len(tn_list))
    if len(df_org) > 0:
        persent_trud.append(round((len(tn_list) * 100.0) / len(df_org), 2))
    else:
        persent_addr.append(0.0)

    df_org = dfa[dfa.rp == razdel]
    print(f"{org_name} - {len(df_org)}")
    df_group = df_org.groupby("tn")
    total_addr_counts.append(len(df_org))
    tn_list, count_list = filter_groups(df_group)
    error_addr_count.append(len(tn_list))
    if len(df_org) > 0:
        persent_addr.append(round((len(tn_list) * 100.0) / len(df_org), 2))
    else:
        persent_addr.append(0.0)

data = {"Дочернее общество": org_names,
        "Общее количество табельных номеров (трудовая деятельность)": total_trud_counts,
        "Ошибки в трудовой деятельности": error_trud_count,
        "Процент труд. деятельность": persent_trud,
        "Общее количество табельных номеров (адреса)": total_addr_counts,
        "Ошибки в адресах": error_addr_count,
        "Процент адреса": persent_addr
        }

df_tn = pd.DataFrame(data)
print(df_tn)
df_tn.to_csv("c:\\github\\errors.csv", sep=";", decimal=",")
