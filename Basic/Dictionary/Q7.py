'''
Q148. Store marks of 5 dierent subjects in a dictionary. Ask subject name
as an input from the User. Print the marks of that subject entered by User.
If subject does not exist, print “Invalid”.

subject_marks_dict = {
"Math": 90,
"English": 85,
"Science": 92,
"History": 88,
"Computer Science": 95

# Example 1
Enter the subject name: Math
Marks for Math: 90

# Example 2
Enter the subject name:
Marks for Math: 90
'''
subject_marks_dict = {
"Math": 90,
"English": 85,
"Science": 92,
"History": 88,
"Computer Science": 95
}
subject = input("Enter the subject name: ")

if subject in subject_marks_dict:
    print(subject_marks_dict[subject])
else:
    print("Invalid")