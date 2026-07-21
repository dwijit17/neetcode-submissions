class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(sub,pick):

            if len(sub)==len(nums):
                ans.append(sub[:])
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    sub.append(nums[i])
                    pick[i] = True
                    backtrack(sub,pick)
                    sub.pop()
                    pick[i] = False
        backtrack([],[False for i in range(len(nums))])
        return ans