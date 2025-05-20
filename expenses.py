def save_expenses():
    password = "helloguys"
    enter_password = input("Enter the password: ")
    if password != enter_password:
        print("Incorrect password. Access denied.")
        return

    expenses = []
    while True:
        expense = input("Enter an expense (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
        try:
            expenses.append(float(expense))
        except ValueError:
            print("Invalid input. Please enter a number.")

    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense}\n")

def read_expenses(filename="expenses.txt"):
    password = "helloguys"
    enter_password = input("Enter the password: ")
    if enter_password != password:
        print("Incorrect password. Access denied.")
        return []

    expenses = []
    try:
        with open(filename, "r") as file:
            for line in file:
                expense = line.strip()
                if expense:
                    expenses.append(float(expense))
    except FileNotFoundError:
        print(f"No expenses found. File {filename} does not exist.")
    except ValueError:
        print("Found invalid data in the file.")

    return expenses

def display_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return

    print("Your Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ${expense:.2f}")

def expense_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(expenses)
    max_expense = max(expenses)
    min_expense = min(expenses)
    average = total / len(expenses)

    print(f"\nSummary:")
    print(f"Total: ${total:.2f}")
    print(f"Max: ${max_expense:.2f}")
    print(f"Min: ${min_expense:.2f}")
    print(f"Average: ${average:.2f}")

def view_expenses():
    expenses = read_expenses()
    display_expenses(expenses)
    expense_summary(expenses)

if __name__ == "__main__":
    view_expenses()
