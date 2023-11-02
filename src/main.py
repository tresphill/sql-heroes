from database.db_connection import execute_query, execute_modify


# Create
def create_hero():
    name = input('Please enter a name for your hero: ')
    about = input('Please enter an about-me: ')
    bio = input('Please enter a short bio: ')
    query = """
            INSERT INTO heroes (name, about_me, biography)
            VALUES (%s, %s, %s);
            """
    create = execute_modify(query, (name, about, bio))
create_hero()

# Read
def select_all_heroes():
    query = """
        SELECT * from heroes
    """
    returned_items = execute_query(query)
    for item in returned_items:
        print(item[1])
    return returned_items

select_all_heroes()


# # Update
def update_hero():
    name_update = input('Which hero would you like to update? ')
    query = """
            UPDATE heroes
            SET name = (%s)
            WHERE name = new_name; 
            """
    new_name = execute_modify(query)
update_hero()

# # Delete
# def delete_hero()