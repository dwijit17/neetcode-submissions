class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        ans = []
        for num in nums:
            hmap[num] = hmap.get(num,0)+1
        
        buckets = [[] for i in range(len(nums))]
        for key in hmap:
            val = hmap[key]
            buckets[val-1].append(key)
        
        for j in range(len(nums)-1,-1,-1):
            curr_bucket = buckets[j]
            #pop out the bucket until k elemnts yougot
            while len(ans)<k and len(curr_bucket)>0:
                ans.append(curr_bucket.pop())
            
            if len(ans)==k:
                return ans

            
                


        