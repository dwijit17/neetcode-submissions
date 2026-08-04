class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in range(1,len(nums)):
            #usually in sum if we add and we get lower sum why add
            #just start new subarray from there
            #but in product we need that min value because later it might
            #become positive value
            prev_max = curr_max
            prev_min = curr_min
            curr_max = max(nums[i],prev_max*nums[i],prev_min*nums[i])
            curr_min = min(nums[i],prev_max*nums[i],prev_min*nums[i])
            ans = max(ans,curr_max)
        return ans