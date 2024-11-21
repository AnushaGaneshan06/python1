# ======================================================TASK MANAGER 2 =========================================================
# Application 02:

#     Note-Taking Application:

#         1. Define the menu: Display the options available to the user.

#         2. Define functions for each operation:
#             View notes
#             Add a new note
#             Search for a note by title
#             Delete a note
        
#         3. Implement the main loop: Continuously prompt the user to choose an option and perform the corresponding action until they choose to exit.

# Expected functios:
#         display_menu(): Prints the main menu.
#         view_notes(notes): Displays all notes with their titles and contents.
#         add_note(notes): Prompts the user to enter a note title and content, then adds the note to the dictionary.
#         search_note(notes): Searches for a note by its title and displays the content if found.
#         delete_note(notes): Deletes a note by its title if it exists in the dictionary.
#         main(): Runs the main loop, displaying the menu and handling user input to perform the appropriate actions.


# =============================================================================================================================

def display_options():
    print("Notes")
    print("===============")
    print("1. View Note")
    print("2. Add a new Note")
    print("3. Search for a note by title")
    print("4. Delete Note")
    print("5. Exit")


def view_note(notes):
    if not notes :
        print("Notes are empty")
    else:
        print("Notes")
        for title, para in notes.items():
            print(f"{title}:{para}")



def add_note(notes):
    title = input("Enter the title for the note: ")
    para = input("Enter the notes to be remember: ")

    if title in notes:
        print("The title already exist")
    else:
        notes[title] = para
        print(f"the note title {title} was added successfully. ")

    
def search_note(notes):
    title = input("Enter the title: ")
    if title in notes :
        print(f"{title}:{notes[title]}")
    else:
        print("Title is not available.")
    

def delete_note(notes):
    title = input("Enter the title to delete")
    if title in notes:
        del notes[title]
        print(f"The note  title {title} was deleted")
    else:
        print("not available")


def main():
    notes = {}

    while True:
        display_options()
        choice = input("Enter the choices (1 - 5): ")

        if choice == "1":
            view_note(notes)

        elif choice == "2":
            add_note(notes)

        elif choice == "3":
            search_note(notes)
        
        elif choice == "4":
            delete_note(notes)

        elif choice == "5":
            print("exit")
            break

        else:
            print("Enter valid choice ")
       



if __name__ == "__main__":
    main()