class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        # ans = None
        for i in range(len(nums)):
            if target-nums[i] in hmap:
                ans = [hmap[target-nums[i]],i]
                return ans
            else:
                hmap[nums[i]] = i
        # return ans


        