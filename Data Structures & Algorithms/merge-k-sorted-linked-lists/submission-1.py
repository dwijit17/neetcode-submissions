# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k==0:
            return None
        happened = True
        dummy = ListNode(-1)
        cpy = dummy
        while happened:
            min_idx = 0
            min_node = None
            minval = float('inf')
            happened = False
            for i in range(k):
                node = lists[i]
                if node:
                    if node.val<=minval:
                        minval = node.val
                        min_node = node
                        min_idx = i
                    happened = True
                    #when it satisfies this condition happened will be true
               
            #after this
            if min_node:
                dummy.next = min_node
                dummy = min_node
                lists[min_idx] = min_node.next
        
        return cpy.next
            

        