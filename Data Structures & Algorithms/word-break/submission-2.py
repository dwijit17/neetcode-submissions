class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = [False]
        memo = {}
        def helper(start):
            if start==len(s):
                ans[0] = True
                return 
            if ans[0]:
                return
            if start in memo:
                return memo[start]
            for i in range(start,len(s)):
                if ans[0]:
                    return
                if s[start:i+1] in wordDict:
                    helper(i+1)
            memo[start] = ans[0]
        helper(0)
        return ans[0]