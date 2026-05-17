class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        ans = []
    
        for i in range(len(nums)):
            heapq.heappush(maxheap, (-nums[i],i))
            if len(maxheap) >= k:
                val = maxheap[0]
                #check if its valid idx in the current heap snapshot
                while maxheap and (not((i-k+1<=val[1]) and (val[1]<=i))):
                    heapq.heappop(maxheap)
                    val = maxheap[0]
                ans.append(-maxheap[0][0])
        return ans
