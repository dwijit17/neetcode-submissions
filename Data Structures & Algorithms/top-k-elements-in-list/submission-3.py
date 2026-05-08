class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0)+1
        
        #use heap
        import heapq
        min_heap = []
        for key in hmap:
            heapq.heappush(min_heap,(hmap[key],key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [ele[1] for ele in min_heap]
        