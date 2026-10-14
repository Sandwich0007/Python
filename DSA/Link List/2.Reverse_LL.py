'''Burte Force'''



# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = head
#         stack = []
#         while temp is not None:
#             stack.append(temp.val)
#             temp = temp.next
#         temp = head
#         while temp is not None:
#             e = stack.pop()
#             temp.val = e
#             temp = temp.next
#         return head
        

'''Optimal'''

class Solution:
    def reverseList(self, head):
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
        