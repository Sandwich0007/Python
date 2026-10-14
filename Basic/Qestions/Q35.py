'''
Q35. Take Salary as input from User and Update the salary of an employee.

salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
'''

salary=int(input("Enter the current salary: "))

if salary<10000:
    increment=5
elif salary>=10000 and salary<20000:
    increment=10
elif salary>=20000 and salary<50000:
    increment=15
elif salary>=50000:
    increment=20

updated_salary=salary+(salary*increment)/100

print(f"Your updated salary is {updated_salary}")