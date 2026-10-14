'''Brute Force'''

# class Solution:
#     def removeNthFromEnd(self, head):
#         length = 0
#         temp = head
#         while temp is not None:
#             length += 1
#             temp = temp.next
#         if length == n:
#             new_head = head.next
#             return new_head
#         position_to_stop = length - n
#         count = 1
#         temp = head
#         while count<position_to_stop:
#             count +=1
#             temp = temp.next
#         temp.next = temp.next.next
#         return head


'''Optimal Solution'''

# class Solution:
#     def removeNthFromEnd(self, head):
#         slow = head
#         fast = head
#         for _ in range(n):
#             fast = fast.next
#         if fast == None:
#             return head.next
#         while fast.next is not None:
#             slow = slow.next
#             fast = fast.next
#         slow.next = slow.next.next
#         return head