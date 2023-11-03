from database.db_connection import execute_modify
from ascii_art import ascii_art
import os
from create_hero import select_all_heroes


def back_to_main():
    print('Enter = Main Menu      Q = Quit \n ')
    prompt = input('').capitalize()
    if prompt == (''):
        main_menu()
    elif prompt == ('Q'):
        quit()

#Create
def create_hero():
    ascii_art()
    print('What Shall We Call You, Traveler?\n ')
    name = input("")
    print('And What Exactly Do You Do?\n ')
    about = input("")
    print('Nice! How About A Short Bio So Other Travelers Know Who You Are?\n ')
    bio = input("")
    query = """
            INSERT INTO heroes (name, about_me, biography)
            VALUES (%s, %s, %s);
            """
    create = execute_modify(query, (name, about, bio))
    print("Succesfully Added Hero\n")
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
    ascii_art()
    select_all_heroes()
    print('Which Hero Would You Like To Update?\n ')
    option = input('')
    print('What Would You Like To Change The Name To?\n ')
    change_name = input('')
    query = """
            UPDATE heroes
            SET name = (%s)
            WHERE id = %s; 
            """
    new_name = execute_modify(query, (change_name, option,))
    print(f'Successfully Changed Hero Name To {change_name}!\n')
    back_to_main()


# # # Delete
def delete_hero():
    ascii_art()
    select_all_heroes()
    print('Which Hero Would You Like To Delete?\n ')
    prompt = input('')
    query = """
            DELETE FROM heroes 
            WHERE id = %s
            """
    delete_hero = execute_modify(query, (prompt,))
    print('Successfully Deleted Hero!\n')
    back_to_main()

def main_menu():
    os.system('clear')
    ascii_art()
    print('Hello World Traveler! What Would You Like To Do?\n')
    print('1- Create A Hero.\n')
    print('2- View All Heroes.\n ')
    print('3- Update A Hero.\n ')
    print('4- Delete Hero.\n ')
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