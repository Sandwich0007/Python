'''Brute Force'''

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         temp = head 
#         mySet = set()
#         while temp is not None:
#             if temp in mySet:
#                 return True
#             mySet.add(temp)
#             temp = temp.next
            
#         return False

'''Optimal Solution'''



class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False