def func(n):
    if n > 10:
        return
    print(n)
    func(n + 1)
n=1
func(n)

# Recursion using tail method 1 to N

# def func(i,n):
#     if n ==0:
#         return
#     func(i,n-1)
#     print(n)

# func(1,5)
