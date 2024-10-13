import sqlite3

DATABASE_PATH='./database.db'
SQL_SCRIPT_PATH='./schema.sql'

def execute_sql_script(script_file):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    with open(script_file, 'r') as f:
        sql_script = f.read()
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    execute_sql_script(SQL_SCRIPT_PATH)