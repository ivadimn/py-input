from datetime import datetime, timedelta

dt_now = datetime.now()
dt = datetime(2022, 8, 28, 11, 45, 0)
delta = (dt_now - dt).seconds / 3600
print(delta)