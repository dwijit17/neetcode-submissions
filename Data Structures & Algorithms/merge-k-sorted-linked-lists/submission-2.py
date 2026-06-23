# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        k = len(lists)
        dummy = ListNode(-1)
        cpy = dummy
        for i in range(k):
            if lists[i]:
                heapq.heappush(min_heap,(lists[i].val,i)) 
        #pushing the k nodes in to heap
        while min_heap:
            nodeval,idx = heapq.heappop(min_heap)
            dummy.next = lists[idx]
            if lists[idx].next:
                heapq.heappush(min_heap,(lists[idx].next.val,idx))
            lists[idx] = lists[idx].next
            dummy = dummy.next
        return cpy.next