import sqlite3

class LibraryModel:
    def __init__(self):
        self.conn = sqlite3.connect("lib.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id TEXT PRIMARY KEY, title TEXT, status TEXT DEFAULT 'Available')")

    def add(self, b_id, title):
        try:
            self.cursor.execute("INSERT INTO books VALUES (?, ?, 'Available')", (b_id, title))
            self.conn.commit()
        except: pass

    def status(self, b_id, st):
        self.cursor.execute("UPDATE books SET status=? WHERE id=?", (st, b_id))
        self.conn.commit()

    def search(self, q):
        self.cursor.execute("SELECT * FROM books WHERE id LIKE ? OR title LIKE ?", (f"%{q}%", f"%{q}%"))
        return self.cursor.fetchall()