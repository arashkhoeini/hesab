
from config import DATABASE_NAME
import sqlite3
import os

class Database(object):

    def __init__(self):
        if not os.path.isfile(DATABASE_NAME):
            con = sqlite3.connect(DATABASE_NAME)
            cur = con.cursor()
            cur.execute('create table \
                    expence(amount text, category text, date text, description text)')
            cur.execute('create table \
                    income(amount text, source text, date text, description text)')
            con.commit()
            con.close()
    
    def get_categories(self):
        con = sqlite3.connect(DATABASE_NAME)
        cur = con.cursor()
        cur.execute('select distinct category from expence')
        result =[cat[0] for cat in cur.fetchall() ]
        con.close()
        return result

    def get_sources(self):
        con = sqlite3.connect(DATABASE_NAME)
        cur = con.cursor()
        cur.execute('select distinct source from income')
        result =[src[0] for src in cur.fetchall() ]
        con.close()
        return result

    def save_expence(self, expence):
        con = sqlite3.connect(DATABASE_NAME)
        cur = con.cursor()
        cur.execute('insert into expence values(?,?,?,?)' ,
                    (expence.amount, expence.category, expence.get_db_date(), expence.description))
        con.commit()
        con.close()

    def save_income(self, income):
        con = sqlite3.connect(DATABASE_NAME)
        cur = con.cursor()
        cur.execute('insert into income values(?,?,?,?)' ,
                    (income.amount, income.source, income.get_db_date(), income.description))
        con.commit()
        con.close()