from database.db_connection import execute_modify
from ascii_art import ascii_art
import os
from create_hero import select_all_heroes


def back_to_main():
    print('Press Enter to return to Main Menu or press Q to quit! ')
    prompt = input('').capitalize()
    if prompt == (''):
        main_menu()
    elif prompt == ('Q'):
        quit()

#Create
def create_hero():
    print('Please enter a name for your hero:\n ')
    name = input("")
    print('Please enter an about-me: ')
    about = input("")
    print('Please enter a short bio: ')
    bio = input("")
    query = """
            INSERT INTO heroes (name, about_me, biography)
            VALUES (%s, %s, %s);
            """
    create = execute_modify(query, (name, about, bio))
    print("Succesfully added Hero")
    back_to_main()

#Read
# def select_all_heroes():
#     query = "SELECT id, name FROM heroes ORDER BY id ASC"
#     names = execute_query(query)
#     for count, x in names:
#         print(f"{count} - {x}")
#     back_to_main()

# # Update
def update_hero():
    select_all_heroes()
    print('Which hero would you like to update?\n ')
    option = input('')
    print('What would you like to change the name to? See list above.\n ')
    change_name = input('')
    query = """
            UPDATE heroes
            SET name = (%s)
            WHERE id = %s; 
            """
    new_name = execute_modify(query, (change_name, option,))
    print(f'Successfully changed hero name to {change_name}')
    back_to_main()


# # # Delete
def delete_hero():
    select_all_heroes()
    print('Which hero would you like to delete?\n ')
    prompt = input('')
    query = """
            DELETE FROM heroes 
            WHERE id = %s
            """
    delete_hero = execute_modify(query, (prompt,))
    print('Successfully deleted hero!')
    back_to_main()

def main_menu():
    os.system('clear')
    ascii_art()
    print('Choose one these options below\n')
    print('1- Create a hero')
    print('2- View all heroes ')
    print('3- Update a hero ')
    print('4- Delete hero ')
    print('Choose an option below: ')
    option = input("")
    if option == '1':
        os.system('clear')
        create_hero()
    elif option == '2':
        os.system('clear')
        select_all_heroes()
        back_to_main()
    elif option == '3':
        os.system('clear')
        update_hero()
    elif option == '4':
        os.system('clear')
        delete_hero()
main_menu()