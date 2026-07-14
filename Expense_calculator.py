import os

# -----------------------------
# Global Variables
# -----------------------------
expenses = []
expense_id = 1


# -----------------------------
# Load Expenses From File
# -----------------------------
def load_expenses():

    global expense_id

    if os.path.exists("expenses.txt"):

        file = open("expenses.txt", "r")

        for line in file:

            line = line.strip()

            if line != "":

                data = line.split(",")

                expense = {
                    "id": int(data[0]),
                    "description": data[1],
                    "amount": float(data[2]),
                    "category": data[3]
                }

                expenses.append(expense)

                expense_id = int(data[0]) + 1

        file.close()


# -----------------------------
# Save Expenses To File
# -----------------------------
def save_expenses():

    file = open("expenses.txt", "w")

    for expense in expenses:

        line = (
            str(expense["id"]) + "," +
            expense["description"] + "," +
            str(expense["amount"]) + "," +
            expense["category"] + "\n"
        )

        file.write(line)

    file.close()

    print("\nExpenses Saved Successfully!\n")


# -----------------------------
# Add Expense
# -----------------------------
def add_expense():

    global expense_id

    print("\n========== ADD EXPENSE ==========")

    description = input("Enter Description: ")

    while True:

        try:

            amount = float(input("Enter Amount (PKR): "))

            if amount <= 0:

                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:

            print("Please enter a valid amount.")

    categories = [
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Education",
        "Other"
    ]

    print("\nCategories")

    for i in range(len(categories)):

        print(str(i + 1) + ". " + categories[i])

    while True:

        try:

            choice = int(input("Choose Category: "))

            if choice >= 1 and choice <= len(categories):

                category = categories[choice - 1]
                break

            else:

                print("Invalid Choice.")

        except ValueError:

            print("Enter Numbers Only.")

    expense = {

        "id": expense_id,
        "description": description,
        "amount": amount,
        "category": category

    }

    expenses.append(expense)

    print("\nExpense Added Successfully!")
    print("Expense ID =", expense_id)

    expense_id += 1
    # -----------------------------
# View All Expenses
# -----------------------------
def view_expenses():

    if len(expenses) == 0:

        print("\nNo Expenses Found.\n")
        return

    print("\n================ ALL EXPENSES ================")
    print("ID\tDescription\tCategory\tAmount")
    print("------------------------------------------------")

    total = 0

    for expense in expenses:

        print(
            str(expense["id"]) + "\t" +
            expense["description"] + "\t\t" +
            expense["category"] + "\t\t" +
            "PKR " + str(expense["amount"])
        )

        total = total + expense["amount"]

    print("------------------------------------------------")
    print("Total Spending = PKR", total)
    print()


# -----------------------------
# Category Summary
# -----------------------------
def category_summary():

    if len(expenses) == 0:

        print("\nNo Expenses Available.\n")
        return

    summary = {}
    total = 0

    for expense in expenses:

        total = total + expense["amount"]

        category = expense["category"]

        if category in summary:

            summary[category] += expense["amount"]

        else:

            summary[category] = expense["amount"]

    print("\n========== CATEGORY SUMMARY ==========")

    for category in summary:

        percentage = (summary[category] / total) * 100

        print(
            category,
            ": PKR",
            summary[category],
            "(" + str(round(percentage, 2)) + "%)"
        )

    print()


# -----------------------------
# Filter By Category
# -----------------------------
def filter_by_category():

    if len(expenses) == 0:

        print("\nNo Expenses Available.\n")
        return

    name = input("Enter Category Name: ")

    found = False
    total = 0

    print("\nMatching Expenses\n")

    for expense in expenses:

        if expense["category"].lower() == name.lower():

            print(
                expense["id"],
                expense["description"],
                expense["category"],
                expense["amount"]
            )

            total += expense["amount"]
            found = True

    if found:

        print("\nTotal =", total)

    else:

        print("No Expense Found In This Category.")

    print()


# -----------------------------
# Delete Expense
# -----------------------------
def delete_expense():

    if len(expenses) == 0:

        print("\nNo Expenses Available.\n")
        return

    view_expenses()

    try:

        delete_id = int(input("\nEnter Expense ID To Delete: "))

    except ValueError:

        print("Invalid ID.")
        return

    for expense in expenses:

        if expense["id"] == delete_id:

            confirm = input("Are you sure? (Y/N): ")

            if confirm.lower() == "y":

                expenses.remove(expense)

                print("Expense Deleted Successfully.\n")

            else:

                print("Deletion Cancelled.\n")

            return

    print("Expense ID Not Found.\n")
    # -----------------------------
# Show Menu
# -----------------------------
def show_menu():

    print("\n===================================")
    print("      PERSONAL EXPENSE TRACKER")
    print("===================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Filter By Category")
    print("5. Delete Expense")
    print("6. Save Expenses")
    print("7. Exit")
    print("===================================")


# -----------------------------
# Main Function
# -----------------------------
def main():

    print("Loading Expenses...")

    load_expenses()

    print("Loaded", len(expenses), "Expenses.\n")

    while True:

        show_menu()

        choice = input("Enter Your Choice (1-7): ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            category_summary()

        elif choice == "4":

            filter_by_category()

        elif choice == "5":

            delete_expense()

        elif choice == "6":

            save_expenses()

        elif choice == "7":

            save_expenses()

            print("\nThank You For Using Expense Tracker!")
            print("Good Bye!")

            break

        else:

            print("\nInvalid Choice! Please Enter 1 to 7.\n")


# -----------------------------
# Program Starts Here
# -----------------------------
if __name__ == "__main__":

    main()