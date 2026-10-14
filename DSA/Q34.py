'''Rotate Image'''
# class Solution:
#     def rotate(self, matrix):
#         n=len(matrix)
#         result=[[0 for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 result[j][(n-1)-i]= matrix[i][j]
#         return result
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(Solution().rotate(matrix))

# This solution will not run in leetcode because we are creating new 
# matrix but they expect to change in the same matrix

'''Optimal Solution'''

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n=len(matrix)
#         for i in range(0,n-1):
#             for j in range(i+1,n):
#                 matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

#         for i in range(n):
#             matrix[i].reverse()