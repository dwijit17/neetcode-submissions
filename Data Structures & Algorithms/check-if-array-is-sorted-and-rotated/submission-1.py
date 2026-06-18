class Solution:
    def check(self, nums: List[int]) -> bool:
        df = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%n]:
                df+=1
        
        return True if df==1 else False
        