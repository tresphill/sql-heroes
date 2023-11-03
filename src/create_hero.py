from database.db_connection import execute_query

def select_all_heroes():
    query = "SELECT id, name FROM heroes ORDER BY id ASC"
    names = execute_query(query)
    for count, x in names:
        print(f"{count} - {x}")