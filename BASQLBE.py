import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY, date TEXT, time TEXT, amount FLOAT, notes TEXT)")

    def insert(self, date, time, amount, notes):
        self.cur.execute("INSERT INTO account VALUES (NULL, ?,?,?,?)",(date, time, amount, notes))

    def view(self):
        self.cur.execute("SELECT * FROM account")
        rows=self.cur.fetchall()
        return rows

    def view_row(self,id):
        self.cur.execute("SELECT * FROM account WHERE id=?",(id,))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM account WHERE id=?",(id,))

    def update(self, date, time, amount, notes, id):
        self.cur.execute("UPDATE account SET date=?, time=?, amount=?, notes=? WHERE id=?", (date, time, amount, notes, id))

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.conn.close()
