'''
Q147. Store “name” of a student as Key, “list of 5 marks” of that student as
a Value. Store atleast 5 student names. Print the sum and percentage of all
the students

students_dict = {
"Student1": [85, 90, 78, 92, 88],
"Student2": [75, 88, 92, 80, 87],
"Student3": [90, 95, 89, 78, 93],
"Student4": [80, 85, 88, 92, 87],
"Student5": [92, 88, 95, 90, 85]

}

# Output
Student1 - Sum: 433, Percentage: 86.60%
Student2 - Sum: 422, Percentage: 84.40%
Student3 - Sum: 445, Percentage: 89.00%
Student4 - Sum: 432, Percentage: 86.40%
Student5 - Sum: 450, Percentage: 90.00%
'''
students_dict = {
"Student1": [85, 90, 78, 92, 88],
"Student2": [75, 88, 92, 80, 87],
"Student3": [90, 95, 89, 78, 93],
"Student4": [80, 85, 88, 92, 87],
"Student5": [92, 88, 95, 90, 85]

}
for name,marks in students_dict.items():
    total = sum(marks)
    percentage = total/500 * 100
    print(f"{name} has score {total} marks and {percentage:.2f}%")
