class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack(sub,start):
        
            if start == len(s):
                ans.append(sub[:])
                return 
                
            for i in range(start,len(s)):
                word = s[start:i+1]
                if word==word[::-1]:
                    sub.append(word)
                    backtrack(sub[:],i+1)
                    sub.pop()
            
        backtrack([],0)
        return ans
        