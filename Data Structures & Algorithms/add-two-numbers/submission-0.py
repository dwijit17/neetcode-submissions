# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = ListNode(-1)
        dummy = prev
        while l1 or l2:
            s = (l1.val if l1 else 0)+(l2.val if l2 else 0) + carry
            val = s%10
            carry = s//10
            if l1:
                l1.val = val
                prev.next = l1
                prev = l1
            else:
                l2.val = val
                prev.next = l2
                prev = l2
            #move pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry!=0:
            prev.next = ListNode(carry)
        return dummy.next