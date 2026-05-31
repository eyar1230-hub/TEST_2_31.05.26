import sqlite3

# The database file that will be created on disk
DB_PATH = "world_cups.db"

# Opens a connection and makes rows behave like dictionaries
def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # lets us use row["column_name"]
    return conn

# Use this for SELECT — returns a list of dicts
def run_query_select(sql, params=()):
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params)  # params prevent SQL injection
        rows = cursor.fetchall()
        return [dict(row) for row in rows]  # convert to plain dicts
    finally:
        conn.close()  # always close, even if an error happens

# Use this for INSERT, UPDATE, DELETE, CREATE
def run_update_query(sql, params=()):
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()  # save changes to disk
        return cursor.lastrowid  # id of the last inserted row
    finally:
        conn.close()

connect()