class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(sub,start):
            ans.append(sub)
            for i in range(start,len(nums)):
                sub.append(nums[i])
                backtrack(sub[:],i+1)
                sub.pop()
        
        backtrack([],0)
        return ans