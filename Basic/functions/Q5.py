'''
Write a function that takes a list of numbers and
prints the sum and average of these numbers
'''
def sum_avg(lst):
    total = 0
    for num in lst:
        total = total + num
    print(f"Total of {lst} is {total}")
    avg = total / len(lst)
    print(f"And the average is {avg}")
sum_avg([2,3,5,8])