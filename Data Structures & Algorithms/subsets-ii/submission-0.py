class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(sub,start):
            ans.append(sub)
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                sub.append(nums[i])
                backtrack(sub[:],i+1)
                sub.pop()
        
        backtrack([],0)
        return ans
        