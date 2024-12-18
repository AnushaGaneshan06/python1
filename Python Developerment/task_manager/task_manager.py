# ================================================TASK MANAGER 1==============================================================
# # Application 01:

#     Steps to Create the Contact Manager Application


#         1. Define the menu: Display the options available to the user.

#         2. Define functions for each operation:
#             View contacts
#             Add a new contact
#             Search for a contact
#             Delete a contact

#         3. Implement the main loop: Continuously prompt the user to choose an option and perform the corresponding action until they choose to exit.


# Expected functios:
#         display_menu(): Prints the main menu.
#         view_contacts(contacts): Displays all contacts.
#         add_contact(contacts): Prompts the user to enter a name and phone number, then adds the contact to the dictionary.
#         search_contact(contacts): Searches for a contact by name and displays the phone number if found.
#         delete_contact(contacts): Deletes a contact by name if it exists in the dictionary.
#         main(): Runs the main loop, displaying the menu and handling user input to perform the appropriate actions.



# # ===========================================================================================================================

def manager_application():
    print("Manager Application")
    print("=============")
    print("1. View contact")
    print("2. Add a new contact")
    print("3. Search for the contact")
    print("4. Delete contact")
    print("5. Exit")


def view_contact(contact):
    if not contact:
        print("the contact is empty")
    else:
        print("Contact")
        for name, number in contact.items():
            print(f"{name}:{number}")
    
   

def add_contact(contact):
    name = input("Enter the name: ")
    number = input ("Enter the number : ")
    if name in contact:
      print("the contact is laready exist")
    else:
        contact[name] = number
        print(f"Contact {name}  is  added successfully .")
       
    
def  search_contact(contact):
    name = input("Enter the contact to search : ")
    if name in contact:
        print(f"{name}:{contact[name]}")
    else:
        print("contact is not available")

def delete_contact(contact):
    name = input("Enter the contact name to delete: ")
    if name in contact:
        del contact[name]
        print(f"The contact {name} was deleted")
    else:
        print("Name has not found in the contact.")



def main():
    contact = {}

    while True:
        manager_application()
        choice = input("Enter the choice to know(1-5): ")


        if choice == "1":
            view_contact(contact)

        elif choice == "2":
            add_contact(contact)

        elif choice == "3":
            search_contact(contact)

        elif choice == "4":
            delete_contact(contact)

        elif choice == "5":
            print("Exit")
            break

        else:
            print("Invalid choice , choice 1 - 5 for the output")

        


if __name__ == "__main__":
    main()



