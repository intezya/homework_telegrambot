import sqlite3

from db.info_to_db import data

data = data[7]


class DataBase:
    def __init__(self, db_name):
        self.db = sqlite3.connect('db/main.db')
        self.cur = self.db.cursor()

    def create_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS homework_table "
            "(date VARCHAR KEY,"
            "column_1 TEXT,"
            "column_2 TEXT,"
            "column_3 TEXT,"
            "column_4 TEXT,"
            "column_5 TEXT,"
            "column_6 TEXT)")

        self.db.commit()

    def add_date(self, date):
        date = data[1]
        self.cur.execute(
            "INSERT INTO homework_table VALUES (?, ?, ?, ?, ?, ?, ?)",
            (date, '', '', '', '', '', ''))
        self.db.commit()

    def add_info(self, info):
        upd_date = info[1]
        c1, c2, c3, c4, c5, c6 = [info[i] for i in range(2, 8)]
        self.cur.execute(f"UPDATE homework_table SET column_1 = ?, "
                         f"column_2 = ?, column_3 = ?, column_4 = ?,"
                         f"column_5 = ?, column_6 = ? "
                         f"WHERE date = ?", (c1, c2, c3, c4, c5, c6, upd_date))
        self.db.commit()

    def get_info(self):
        self.cur.execute("SELECT * FROM homework_table")
        return self.cur.fetchall()


if __name__ == '__main__':
    d = DataBase('main.db')
    print(d.get_info())
