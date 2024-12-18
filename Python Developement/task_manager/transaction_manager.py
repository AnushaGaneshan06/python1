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
    print("transaction manager")
    print("=================")
    print("1. View transaction")
    print("2. Add new transaction")
    print("3. Edit transaction")
    print("4. delete transaction")
    print("5. Total balance transaction")
    print("6. Exit")

def view_transcation(transactions):
    if not transactions:
        print("transaction is empty")
    else:
        for i, transaction in enumerate(transactions):
            print(f"{i + 1} {transaction['category']} - {transaction['amount']} - {transaction['description']}")


def  add_new_transaction(transactions):
    category = input("Enter the category: ")
    amount = float(input("enter the amount: "))
    description = input("enter the description:")
    transactions.append({"category":category, "amount":amount, "description": description})
    print("the transaction is updated successfully")

    

def edit_transaction(transactions):
    view_transcation(transactions)
    index = int(input("enter the index number: ")) -1
    if 0 <= index < len(transactions):
        category = input(f"enter new category(current:{transactions[index]['category']}")  
        amount = float(input(f"enter the new amount (current:{transactions[index]['amount']})"))
        description = input(f"enter the new description (current:{transactions[index]['description']})")
        transactions[index] = ({"category":category, "amount":amount, "description":description})
        print("transaction updated")

    else:
        print("invalid")



def delete_transaction(transcations):
    view_transcation(transcations)
    index = int(input("enter the index value: ")) -1
    if 0 <= index < len(transcations):
        deleted = transcations.pop(index)
        print(f"{deleted} was deleted")
    else:
        print("invalid")
    


def  total_balance_transaction(transactions):
    total = sum(transaction["amount"] for transaction in transactions)
    print(f"\nTotal Balance: {total}")



def main():
    transactions = []

    while True:
        display_option()
        choice = input("enter the choice (1 -5 ): ")


        if choice == "1":
            view_transcation(transactions)

        elif choice == "2":
            add_new_transaction(transactions)

        elif choice == "3":
            edit_transaction(transactions)

        elif choice == "4":
            delete_transaction(transactions)

        elif choice == "5":
            total_balance_transaction(transactions)

        elif choice == "6":
            print("exit")
            break
        else:
            print("enter valid choice")





if __name__ == "__main__":
    main()