
from pathlib import Path
import pandas as pd

# Step 1: Locate our financial CSV file
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "raw" / "corporate_transactions.csv"

# Step 2: Read the CSV file using Pandas
df = pd.read_csv(file_path)

# Step 3: Display all transactions
print("CORPORATE FINANCIAL TRANSACTIONS")
print(df)

# Step 4: Calculate total revenue
revenue = df.loc[df["transaction_type"] == "Revenue", "amount"].sum()

# Step 5: Calculate total expenses
expenses = df.loc[df["transaction_type"] == "Expense", "amount"].sum()

# Step 6: Calculate profit
profit = revenue - expenses

# Step 7: Display financial results
print("\nFINANCIAL PERFORMANCE SUMMARY")
print(f"Total Revenue: ${revenue:,.2f}")
print(f"Total Expenses: ${expenses:,.2f}")
print(f"Total Profit: ${profit:,.2f}")
