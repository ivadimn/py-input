from datetime import datetime, timedelta
from pprint import pprint

dt = datetime.strptime("{0}.{1}.01".format(datetime.now().year, datetime.now().month), "%Y.%m.%d")
ts = dt.timestamp()
dt1 = datetime.fromtimestamp(ts)
print(dt1.year)
print(dt1.month)
print(dt1.day)
print(dt1.weekday())
cal = []
cal.append(["<<", str(dt.year), ">>"])
cal.append(["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"])
days = [[" " for _ in range(7)] for _ in range(5)]
print(days)
curr_month = dt.month
delta = timedelta(days=1)
curr_week = 0
while dt.month == curr_month:
    wd = dt.weekday()
    print(curr_week, wd)
    days[curr_week][wd] = str(dt.day)
    dt = dt + delta
    if wd == 6:
        curr_week += 1


pprint(days)