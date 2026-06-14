import os

expenses = []


def load_expenses():

    if os.path.exists("expenses.txt"):

        with open("expenses.txt", "r") as file:

            for line in file:

                line = line.strip()

                if line:

                    parts = line.split("|")

                    expense = {
                        "id": int(parts[0]),
                        "amount": float(parts[1]),
                        "category": parts[2],
                        "date": parts[3],
                        "note": parts[4]
                    }

                    expenses.append(expense)


def save_expenses():

    with open("expenses.txt", "w") as file:

        for expense in expenses:

            file.write(
                f"{expense['id']}|"
                f"{expense['amount']}|"
                f"{expense['category']}|"
                f"{expense['date']}|"
                f"{expense['note']}\n"
            )


def add_expense():

    try:

        amount = float(
            input("Enter Expense Amount: ")
        )

        category = input(
            "Enter Category (Food/Travel/Shopping/etc): "
        )

        date = input(
            "Enter Date (DD-MM-YYYY): "
        )

        note = input(
            "Enter Note: "
        )

        next_id = 1

        if expenses:

            next_id = (
                max(exp["id"] for exp in expenses)
                + 1
            )

        expense = {

            "id": next_id,
            "amount": amount,
            "category": category,
            "date": date,
            "note": note
        }

        expenses.append(expense)

        save_expenses()

        print("Expense Added Successfully!")

    except ValueError:

        print("Invalid Amount!")


def view_expenses():

    if not expenses:

        print("No Expenses Found!")
        return

    print("\n===== ALL EXPENSES =====")

    for expense in expenses:

        print(
            f"ID: {expense['id']} | "
            f"Amount: ₹{expense['amount']} | "
            f"Category: {expense['category']} | "
            f"Date: {expense['date']} | "
            f"Note: {expense['note']}"
        )


def search_expense():

    keyword = input(
        "Enter Category or Note: "
    ).lower()

    found = False

    for expense in expenses:

        if (
            keyword in expense["category"].lower()
            or
            keyword in expense["note"].lower()
        ):

            print(
                f"ID: {expense['id']} | "
                f"₹{expense['amount']} | "
                f"{expense['category']} | "
                f"{expense['date']} | "
                f"{expense['note']}"
            )

            found = True

    if not found:

        print("No Matching Expense Found!")


def delete_expense():

    try:

        expense_id = int(
            input("Enter Expense ID to Delete: ")
        )

        for expense in expenses:

            if expense["id"] == expense_id:

                expenses.remove(expense)

                save_expenses()

                print("Expense Deleted!")

                return

        print("Expense Not Found!")

    except ValueError:

        print("Invalid Input!")


def total_expense():

    total = 0

    for expense in expenses:

        total += expense["amount"]

    print(
        f"\nTotal Expense: ₹{total}"
    )


def expense_statistics():

    if not expenses:

        print("No Expenses Available!")
        return

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    highest = max(
        expense["amount"]
        for expense in expenses
    )

    lowest = min(
        expense["amount"]
        for expense in expenses
    )

    average = total / len(expenses)

    print("\n===== EXPENSE STATISTICS =====")

    print(f"Total Expenses : ₹{total}")

    print(f"Highest Expense : ₹{highest}")

    print(f"Lowest Expense : ₹{lowest}")

    print(
        f"Average Expense : ₹{average:.2f}"
    )


def category_summary():

    if not expenses:

        print("No Expenses Available!")
        return

    summary = {}

    for expense in expenses:

        category = expense["category"]

        if category not in summary:

            summary[category] = 0

        summary[category] += expense["amount"]

    print("\n===== CATEGORY SUMMARY =====")

    for category, amount in summary.items():

        print(
            f"{category} : ₹{amount}"
        )


def menu():

    while True:

        print("\n")
        print("=" * 40)
        print("      EXPENSE TRACKER SYSTEM")
        print("=" * 40)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Total Expense")
        print("6. Expense Statistics")
        print("7. Category Summary")
        print("8. Exit")

        choice = input(
            "Enter Your Choice: "
        )

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            search_expense()

        elif choice == "4":

            delete_expense()

        elif choice == "5":

            total_expense()

        elif choice == "6":

            expense_statistics()

        elif choice == "7":

            category_summary()

        elif choice == "8":

            print("Thank You!")

            break

        else:

            print("Invalid Choice!")


load_expenses()
menu()