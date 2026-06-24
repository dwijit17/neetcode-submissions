# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseK(head,k):
            #check if size exist
            exist = False
            count = 0
            curr = head
            while curr:
                curr = curr.next
                count+=1
                if count==k:
                    exist = True
                    break
            
            #if that size exists then do the reverse operation
            prev = None
            count = 0
            curr = head
            if exist:
                while curr and count<k:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                    count+=1
                return (head,prev,curr,True)
            return (head,prev,curr,False)
        dpt = ListNode(-1)
        cpy = dpt
        while head:
            tail,prev,curr,rv = reverseK(head,k)
            if rv:
                dpt.next = prev
                dpt = tail
                head = curr
            else:
                dpt.next = tail
                break

        return cpy.next



        