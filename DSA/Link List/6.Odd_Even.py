'''Brute Force'''


# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head
#         value = []
#         temp = head
#         while temp:
#             value.append(temp.val)
#             if temp.next:
#                 temp = temp.next.next
#             else:
#                 break
#         temp = head.next
#         while temp:
#             value.append(temp.val)
#             if temp.next:
#                 temp = temp.next.next
#             else:
#                 break
#         temp = head 
#         index = 0
#         while temp is not None:
#             temp.val = value[index]
#             index +=1
#             temp = temp.next
#         return head

        
'''Optimal'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head
        


        


        