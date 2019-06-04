# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.r = ListNode(None)
        
       
        cursor = head
        while cursor != None:
            t = ListNode(cursor.val)
            t.next = self.r
            self.r = t
            cursor = cursor.next
        
        # to output reversedLinkedList as a list
        lst = []
        cursor = self.r
        while cursor.val != None:
            lst.append(cursor.val)
            cursor = cursor.next
            
        return lst
        