import pandas as pd
import matplotlib.pyplot as plt


def load_expense_data(file_path):
    df = pd.read_csv(file_path)
    return df


def clean_expense_data(df):
    df["amount"] = df["amount"].fillna(0)
    df["date"] = pd.to_datetime(df["date"])
    return df


def calculate_total_expense(df):
    total_expense = df["amount"].sum()
    return total_expense


def calculate_category_summary(df):
    category_summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    return category_summary


def calculate_payment_method_summary(df):
    payment_summary = df.groupby("payment_method")["amount"].sum().sort_values(ascending=False)
    return payment_summary


def show_basic_report(df, total_expense, category_summary, payment_summary):
    print("\nSTUDENT BUDGET ANALYSIS REPORT")
    print("-" * 40)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nTotal expense:")
    print(f"{total_expense:.2f} TL")

    print("\nExpense by category:")
    print(category_summary)

    print("\nExpense by payment method:")
    print(payment_summary)

    highest_category = category_summary.idxmax()
    highest_amount = category_summary.max()

    print("\nHighest spending category:")
    print(f"{highest_category} - {highest_amount:.2f} TL")


def create_category_chart(category_summary):
    plt.figure(figsize=(8, 5))
    category_summary.plot(kind="bar")
    plt.title("Total Expense by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("category_expenses.png")
    plt.show()


def create_payment_method_chart(payment_summary):
    plt.figure(figsize=(6, 5))
    payment_summary.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expense Distribution by Payment Method")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("payment_methods.png")
    plt.show()


def main():
    file_path = "expenses.csv"

    df = load_expense_data(file_path)
    df = clean_expense_data(df)

    total_expense = calculate_total_expense(df)
    category_summary = calculate_category_summary(df)
    payment_summary = calculate_payment_method_summary(df)

    show_basic_report(df, total_expense, category_summary, payment_summary)

    create_category_chart(category_summary)
    create_payment_method_chart(payment_summary)


if __name__ == "__main__":
    main()