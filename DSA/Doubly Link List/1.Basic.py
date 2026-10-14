'''Node Structure'''

# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#         self.prev = None

'''Basic Operaion'''

'''Insert at head'''

# class Node:
#     def insert_at_head(self,val):
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

'''Insert At End'''

# class Node:
#     def insert_at_end(self,val):
#         new_node = Node(val)
#         if not self.head:
#             new_node = self.head
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node
#             new_node.prev = temp

class Node:
    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            count +=1
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

        


