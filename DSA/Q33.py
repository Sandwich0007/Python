'''
Set Matrix Zeroes
'''

# class Solution:
#     def markInfinity(self,matrix,row,col):
#         r = len(matrix)
#         c = len(matrix[0])
#         for i in range(0,r):
#             if matrix[i][col]!=0:
#                 matrix[i][col]=float("inf")
#         for j in range(0,c):
#             if matrix[row][j]!=0:
#                 matrix[row][j]=float("inf")

#     def setZeroes(self, matrix):
#         r = len(matrix)
#         c = len(matrix[0])
#         for i in range(0,r):
#             for j in range(0,c):
#                 if matrix[i][j]==0:
#                     self.markInfinity(matrix,i,j)

#         for i in range(0,r):
#             for j in range(0,c):
#                 if matrix[i][j]==float("inf"):
#                     matrix[i][j]=0
#         return matrix

'''
Optimal Solution
'''

# class Solution:
#     def setZeroes(self, matrix):
#         r = len(matrix)
#         c = len(matrix[0])
#         rowTrack = [0 for _ in range(r)]
#         colTrack = [0 for _ in range(c)]
#         for i in range(r):
#             for j in range(c):
#                 if matrix[i][j]==0:
#                     rowTrack[i]=-1
#                     colTrack[j]=-1
#         for i in range(r):
#             for j in range(c):
#                 if rowTrack[i]==-1 or colTrack[j]==-1:
#                     matrix[i][j]=0
#         return matrix