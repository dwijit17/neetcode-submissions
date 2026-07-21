class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(start,sub,target):
            if target<0:
                return
    
            if target==0:
                ans.append(sub[:])
    
            for i in range(start,len(nums)):
                if i>0 and (i>start and nums[i]==nums[i-1]):
                    continue
                sub.append(nums[i])
                backtrack(i+1,sub[:],target-nums[i])
                sub.pop()
        
        backtrack(0,[],target)
        return ans
        