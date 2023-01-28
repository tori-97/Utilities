import sqlite3, os
from threading import Lock


DATABASE_TABLES = "<tables_path>"
DATABASE_FILES  = "<raw_files_path>"

class DatabaseTemplate():
    def __init__(self, name: str) -> None:
        self._name = name
        self.FILE_PATH = os.path.join(DATABASE_FILES, f"{self._name}.db") 
        
        self._db = sqlite3.connect(self.FILE_PATH, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._cursor = self._db.cursor()

        self._locker = Lock()

    def getAllTables(self):
        SQL = "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
        conn = self._cursor.execute(SQL)
        _rows = conn.fetchall()
        rows = []

        for r in _rows:
            rows.append(dict(r).get('name'))

        return rows

    def execute(self, sql, *params):
        try:
            return self._cursor.execute(sql, params)
        except sqlite3.OperationalError as e:
            return None

    def executeAndSave(self, sql, *params):
        try:
            self._locker.acquire()
            self._cursor.execute(sql, params)
            self._db.commit()
            self._locker.release()
        except sqlite3.OperationalError as e:
            # print(f"SQLERROR: {e}")
            return False
        
        return True

    def fetchone(self, sql, *params):
        result = self.execute(sql, *params)

        if result is not None:
            fetched = result.fetchone()
            if fetched is not None:
                fetched = dict(fetched)
            return fetched
        return None

    def fetchall(self, sql, *params):
        _rows = self.execute(sql, *params).fetchall()
        rows = []
        for row in _rows:
            rows.append(dict(row))
        
        return rows

    def createTables(self, tables: str):
        with open(os.path.join(DATABASE_TABLES,  f"{tables}.sql")) as f:
            data = f.read()
        self._cursor.executescript(data)
    
    def save(self):
        self._db.commit()
        
    def close(self):
        self._db.close()
