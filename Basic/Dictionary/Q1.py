'''
Q142. Ask subject name and marks from the user and keep adding it to
dictionary.

Enter the number of subjects: 4
Enter the subject name: Maths
Enter the marks for Maths: 22
Enter the subject name: English
Enter the marks for English: 98
Enter the subject name: Computer
Enter the marks for Computer: 87
Enter the subject name: Science
Enter the marks for Science: 66

# Output
{'Maths': 22.0, 'English' : 98.0, 'Computer' : 87.0, 'Science': 66.0}
'''
subjects = int(input("Enter the number of subjects : "))

result = {}

for i in range(0,subjects):
    subjects_name = input("Enter the subject name : ")
    subjects_marks = int(input(f"Enter the marks for {subjects_name} : "))
    result[subjects_name] = subjects_marks

print(result)