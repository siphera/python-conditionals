# declaring my variables
annual_salary = float(input("enter annual salary: "))
employment_type = input("please enter employment type: ")

monthly_salary = annual_salary // 12
print("monthly net salary: ", round(monthly_salary, 2))

if employment_type.upper() == 'P':
    total = monthly_salary * 0.295
    grand_total = monthly_salary - total
    print("monthly gross: ",  round(grand_total, 2))

elif employment_type.upper() == 'O':
    total = monthly_salary * 0.25
    grand_total = monthly_salary - total
    print("monthly gross salary: ", round(grand_total, 2))

# print("monthly net salary: ", monthly_salary)
