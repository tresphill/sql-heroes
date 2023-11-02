from database.db_connection import execute_query, execute_modify

def main_menu():
    print('Choose one these options below\n')
    print('1- Create a hero')
    input = ('Choose an option below: ')
    if input == '1':
        create_hero()
main_menu()



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





# Read
def select_all_heroes():
    query = """
        SELECT * from heroes
    """
    returned_items = execute_query(query)
    for item in returned_items:
        print(item[1])
    return returned_items




# # Update
def update_hero():
    name_update = input('Which hero would you like to update? ')
    query = """
            UPDATE heroes
            SET name = (%s)
            WHERE name = new_name; 
            """
    new_name = execute_modify(query)


# # Delete
# def delete_hero()