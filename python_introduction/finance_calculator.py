monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
# Assuming a simple annual interest of 5%
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Monthly savings = ", monthly_savings)
print(projected_savings)
