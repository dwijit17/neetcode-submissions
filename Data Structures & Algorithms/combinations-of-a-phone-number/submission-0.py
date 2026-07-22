class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits)==0:
            return ans
        hmap = {
            2 :"abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        def backtrack(sub,start):

            if len(sub) == len(digits):
                ans.append("".join(sub[:]))
                return
        
            for i in range(start,len(digits)):
                chars = hmap[int(digits[i])]
                for ch in chars:
                    sub.append(ch)
                    backtrack(sub[:],i+1)
                    sub.pop()
            
        backtrack([],0)
        return ans
            