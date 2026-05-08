class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        # ans = None
        for i in range(len(nums)):
            if target-nums[i] in hmap:
                ans = [i,hmap[target-nums[i]]]
                ans.sort()
                return ans
            else:
                hmap[nums[i]] = i
        # return ans


        