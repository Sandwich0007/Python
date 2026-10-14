'''Brute Force'''

# class Solution:
#     def detectCycle(self, head):
#         temp = head 
#         mySet = set()
#         while temp is not None:
#             if temp in mySet:
#                 return temp
#             mySet.add(temp)
#             temp = temp.next
            
#         return None

'''Optimal Solution'''

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None