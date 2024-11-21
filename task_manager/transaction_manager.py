# =======================================================TASK MANAGER 03 ======================================================
# Application 03:

# Personal Budget Tracker:
#     Define the Menu: Display the options available to the user.

# Define Functions for Each Operation:

#     View all transactions
#     Add a new transaction
#     Edit an existing transaction
#     Delete a transaction
#     View the total balance

# Implement the Main Loop: Continuously prompt the user to choose an option and perform the corresponding action until they choose to exit.

# Expected Functions:
#     display_menu(): Prints the main menu.
#     view_transactions(transactions): Displays all transactions with their categories, amounts, and descriptions.
#     add_transaction(transactions): Prompts the user to enter a transaction category, amount, and description, then adds the transaction to the list.
#     edit_transaction(transactions): Allows the user to modify an existing transaction’s details based on its index or title.
#     delete_transaction(transactions): Deletes a transaction by its index or title if it exists in the list.
#     view_balance(transactions): Calculates and displays the total balance, which is the sum of all transactions.
#     main(): Runs the main loop, displaying the menu and handling user input to perform the appropriate actions.


# ===========================================================================================================================



def display_option():
    print("Transaction")
    print("================")
    print("1. View Transaction")
    print("2. Add new Transaction")
    print("3. Edit Existing Transaction")
    print("4. Delete Transaction")
    print("5. View Total Balance")
    print("6.Exit")


def  view_transaction():
    pass



def add_new_transaction():
    pass



def  edit_transaction():
    pass


def  delete_transaction():
    pass

def total_balance_transaction():
    pass




def main():
    transaction = {}

    while True:
        display_option()
        choice = input("Enter the Choice between (1 -5 ): ")

        if choice == "1":
            view_transaction()

        elif choice == "2":
            add_new_transaction()

        elif choice == "3":
            edit_transaction()

        elif choice == "4":
            delete_transaction()

        elif choice == "5":
            total_balance_transaction()
        
        elif choice == "6":
            print("exit")
            break

        else:
            print("invalid choice")





if __name__ == "__main__":
    main()