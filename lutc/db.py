from datetime import datetime
import requests.exceptions
from requests import request, codes
import sqlite3

def query_db(sql: str, params: dict) -> list:
    try:
        with sqlite3.connect("sessions.db") as conn:
            if len(params) > 0:
                cursor = conn.execute(sql, params.values())
            else:
                cursor = conn.execute(sql)
        return cursor.fetchall()
    except:
        return []

sql_insert = "INSERT INTO  VALUES ".format(user_table["NAME"])