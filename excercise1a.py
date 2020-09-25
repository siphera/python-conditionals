annual_salary = float(input("enter annual salary: "))
monthly_salary = annual_salary / 12
# print(monthly_salary)

amount = annual_salary
if amount >= 100000:
    total = monthly_salary * 0.295
    grand_total = monthly_salary - total
    print("monthly gross: ", grand_total)

elif amount <= 80000:
    total = monthly_salary * 0.25
    grand_total = monthly_salary - total
    print("monthly gross: ", grand_total)
