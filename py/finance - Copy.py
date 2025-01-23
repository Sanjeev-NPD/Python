import json
import os
import csv

# Define the file to store data
DATA_FILE = 'finance_data.json'
CSV_FILE = 'finance_data.csv'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {"income": [], "expenses": []}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_entry(entry_type, amount, description):
    data = load_data()
    entry = {"amount": amount, "description": description}
    if entry_type == "income":
        data["income"].append(entry)
    elif entry_type == "expense":
        data["expenses"].append(entry)
    else:
        print("Invalid entry type. Use 'income' or 'expense'.")
        return
    save_data(data)
    print(f"{entry_type.capitalize()} entry added.")

def view_summary():
    data = load_data()
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    balance = total_income - total_expenses
    print("\nFinancial Summary:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}\n")

def generate_csv():
    data = load_data()
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Description"])
        for entry in data["income"]:
            writer.writerow(["Income", entry["amount"], entry["description"]])
        for entry in data["expenses"]:
            writer.writerow(["Expense", entry["amount"], entry["description"]])
    print(f"CSV file '{CSV_FILE}' has been generated.")

def main():
    while True:
        print("Personal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Generate CSV")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            while True:
                amount = float(input("Enter income amount: "))
                description = input("Enter description: ")
                add_entry("income", amount, description)
                another = input("Add another income entry? (y/n): ").lower()
                if another != 'y':
                    break
        elif choice == "2":
            while True:
                amount = float(input("Enter expense amount: "))
                description = input("Enter description: ")
                add_entry("expense", amount, description)
                another = input("Add another expense entry? (y/n): ").lower()
                if another != 'y':
                    break
        elif choice == "3":
            view_summary()
        elif choice == "4":
            generate_csv()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
