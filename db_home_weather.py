import pymysql.cursors
import pandas as pd

class db_home_weather:

    def __init__(self):
        self.connection = pymysql.connect(
            host='Nate-PC'
            ,user='admin'
            ,password='gsfpAupsE9edYed098!@#'
            ,db='home_weather'
            ,charset='utf8'
            ,cursorclass=pymysql.cursors.DictCursor
        )

    def run_sql(self, sql, auto_commit=True):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)

        if auto_commit:
            self.connection.commit()

    def close_connection(self):
        self.connection.close()