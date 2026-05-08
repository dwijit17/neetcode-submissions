class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0)+1
        
        #sort the hmap based on key
        hmap = sorted(hmap , key = lambda item: hmap[item],reverse = True)
        return hmap[:k]

        