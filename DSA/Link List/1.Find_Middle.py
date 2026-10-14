'''Brute Force'''


# class Solution:
#     def middleNode(self, head):
#         temp = head
#         n = 0
#         while temp is not None:
#             n += 1
#             temp = temp.next
#         temp = head
#         for i in range(n//2):
#             temp = temp.next
#         return temp

'''Optimal Solution'''

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

        