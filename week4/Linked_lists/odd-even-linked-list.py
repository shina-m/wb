# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head != None and head.next != None:
            odd = head
            even = head.next
            while even != None and even.next != None:
                t = even.next
                even.next = even.next.next if even.next.next != None else None
                t.next = odd.next
                odd.next = t

                odd = odd.next
                even = even.next
            
        # to output reversedLinkedList as a list
        lst = []
        cursor = head
        while cursor != None:
            lst.append(cursor.val)
            cursor = cursor.next
            
        return lst
            
        
        