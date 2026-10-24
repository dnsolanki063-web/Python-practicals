#assignment pre_3
base_salary = float(input("Enter the basic salary: "))
years = int(input("Enter the number of years: "))
if years < 2:
    bonus = base_salary * 5/100
elif years <= 5:
    bonus = base_salary * 10 / 100
elif years <= 10:
    bonus = base_salary * 15 / 100
else:
    bonus = base_salary * 20 / 100
gross_salary = base_salary + bonus
print("Basic Salary =", base_salary)
print("Bonus =", bonus)
print("Gross Salary =", gross_salary)
