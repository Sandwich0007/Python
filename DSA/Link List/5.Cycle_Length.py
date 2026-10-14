'''Brute Force'''

# class Solution:
#     def lengthOfLoop(self, head):
#         myDict = {}
#         temp = head
#         travel = 0
#         while temp is not None:
#             if temp in myDict:
#                 return travel - myDict[temp]
#             else:
#                 myDict[temp] = travel
#                 travel +=1
#                 temp = temp.next
        
#         return 0

'''Optimal Solution'''

class Solution:
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow!=fast:
                    slow = slow.next
                    count +=1
                return count
        return 0