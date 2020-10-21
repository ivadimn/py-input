import pandas as pd

file_trud = 'C:\\github\\trud1.csv'
file_addr = 'C:\\github\\addr1.csv'
orgs = {
    'ООО "Газпром добывча Астрахань"': 'Газпром добыча Астрахань',
    'ООО "Газпром добывча Иркутск"': 'Газпром добыча Иркутск',
    'ООО "Газпром добывча Краснодар"': 'Газпром добыча Краснодар',
    'ООО "Газпром добывча Надым"': 'Газпром добыча Надым',
    'ООО "Газпром добывча Ноябрьск"': 'Газпром добыча Ноябрьск',
    'ООО "Газпром добывча Уренгой"': 'Газпром добыча Уренгой',
    'ООО "Газпром добывча Ямбург"': 'Газпром добыча Ямбург',
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
    'OOO "Газпром переработка"': 'Газпром переработка'
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
dfa = pd.read_csv(file_addr, sep=";")
for org_name, org in orgs.items():
    df_org = df[df.org == org]
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

    df_org = dfa[dfa.org == org]
    print(f"{org_name} - {len(df_org)}")
    df_group = df_org.groupby("tn")
    total_addr_counts.append(len(df_org))
    tn_list, count_list = filter_groups(df_group)
    error_addr_count.append(len(tn_list))
    if len(df_org) > 0:
        persent_addr.append(round((len(tn_list) * 100.0) / len(df_org), 3))
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
