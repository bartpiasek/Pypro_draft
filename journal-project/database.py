import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    """
    docstring
    """
    with connection: #COMMIT QUERY "CREATE TABLE"
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(entry_content, entry_date):
    """
    docstring
    """
    with connection:
        # connection.execute(f"INSERT INTO entries VALUES('{entry_content}', '{entry_date}');") - SQL injection
        connection.execute(
            "INSERT INTO entries VALUES(?, ?);", (entry_content, entry_date)
        )

def get_entries():
    """
    docstring
    """
    cursor = connection.execute("SELECT * FROM entries;")
    # return cursor.fetchall()
    return cursor
    
