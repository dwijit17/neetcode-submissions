class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(start,sub,target):
            if target<0:
                return
    
            if target==0:
                ans.append(sub[:])
            
            for i in range(start,len(nums)):
                sub.append(nums[i])
                backtrack(i,sub[:],target-nums[i])
                sub.pop()
        
        backtrack(0,[],target)
        return ans
        