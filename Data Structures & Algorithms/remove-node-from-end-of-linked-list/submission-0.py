# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #nth node from end of list
        #4 elemens 2 nd node from end means 3 rd node from start 
        #how 4-2+1 = 3
        #1 2 n = 2 2-2+1 = 1st node from start 1 based indexing
        #for that we need to get the length of llist
        #better idea maintain the differnce of n using tow pointesrs
        #when fast pointer reaches end slow pointer will be on the n th node from end
        #remove that node
        dummy = ListNode(val=-1)
        dummy.next = head
        s = dummy
        f = dummy
        count = 0
        while f:
            if count==n+1:
                break
            f = f.next
            count+=1
        
        while f:
            f = f.next
            s = s.next
        
        if s and s.next:
            s.next = s.next.next
        else:
            s.next= None
        
        return dummy.next


        