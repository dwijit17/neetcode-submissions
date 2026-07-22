class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(sub,o,c):

            if o==0 and c==0:
                ans.append("".join(sub[:]))
                return
            
            if o<0 or c<0:
                return

            if o>c:
                return 

            sub.append("(")
            backtrack(sub[:],o-1,c)
            sub.pop()
            sub.append(")")
            backtrack(sub[:],o,c-1)
        
        backtrack([],n,n)
        return ans
        