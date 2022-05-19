from datetime import datetime
import requests.exceptions
from requests import request, codes
import sqlite3

def query_db(sql: str, params: dict) -> list:
    try:
        with sqlite3.connect("sessions.db") as conn:
            if len(params) > 0:
                cursor = conn.execute(sql, tuple(params.values()))
            else:
                cursor = conn.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as ex:
        print(ex.args[0])
        return []

sql_insert = "INSERT INTO cities(name, write_at) VALUES (?, ?)"
id_select = "SELECT last_insert_rowid() from cities"
c = ["Moscow-3", "Rome-4", "Paris-4"]

for i in range(3):
    p = {"name" : c[i], "write_at": datetime.now().timestamp() }
    r = query_db(sql_insert, p)
    print(r)
    r_id = query_db(id_select, {})
    print(r_id)

