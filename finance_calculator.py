# finance_calculator.py
# Prompt user for financial data
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
# Calculate annual projection with a 5% interest rate
annual_savings = monthly_savings * 12
projected_savings = annual_savings * 1.05
# Display results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected annual savings with 5% interest: ${projected_savings:.2f}")
