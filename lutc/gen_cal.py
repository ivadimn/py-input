from datetime import datetime, timedelta
from pprint import pprint

dt = datetime.strptime("01.{0}.{1}".format(datetime.now().month, datetime.now().year), "%d.%m.%Y")
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday())
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