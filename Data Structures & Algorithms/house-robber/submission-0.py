class Solution:
    def rob(self, nums: List[int]) -> int:
        hmap = {}
        nums.append(0)
        nums.append(0)
        def money(i):
            if i<0:
                return 0
            if i in hmap:
                return hmap[i]
            
            m = max(nums[i]+money(i-2),money(i-1))
            hmap[i] = m
            return hmap[i]
        ans  = money(len(nums)-1)
        # print(hmap)
        return ans