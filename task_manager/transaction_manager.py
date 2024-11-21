Application 03:

Personal Budget Tracker:
    Define the Menu: Display the options available to the user.

Define Functions for Each Operation:

    View all transactions
    Add a new transaction
    Edit an existing transaction
    Delete a transaction
    View the total balance

Implement the Main Loop: Continuously prompt the user to choose an option and perform the corresponding action until they choose to exit.

Expected Functions:
    display_menu(): Prints the main menu.
    view_transactions(transactions): Displays all transactions with their categories, amounts, and descriptions.
    add_transaction(transactions): Prompts the user to enter a transaction category, amount, and description, then adds the transaction to the list.
    edit_transaction(transactions): Allows the user to modify an existing transaction’s details based on its index or title.
    delete_transaction(transactions): Deletes a transaction by its index or title if it exists in the list.
    view_balance(transactions): Calculates and displays the total balance, which is the sum of all transactions.
    main(): Runs the main loop, displaying the menu and handling user input to perform the appropriate actions.
