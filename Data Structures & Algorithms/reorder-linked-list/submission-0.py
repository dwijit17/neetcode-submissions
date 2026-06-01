# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #go to half and reverse the list
        s = head
        f = head
        cpy = head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        head2 = s.next
        s.next = None

        prev = None
        while head2:
            nxt_node = head2.next
            head2.next = prev
            prev = head2
            head2 = nxt_node
        #now prev has the last node now iterest accordingly
        while head and prev:
            headnn = head.next
            prevnn = prev.next
            head.next = prev
            prev.next = headnn
            head = headnn
            prev = prevnn
        
            
        

            
        