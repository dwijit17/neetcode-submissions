class Solution:
    def climbStairs(self, n: int) -> int:
        hmap = {}
        def ways(n):
            if n==0 or n==1:
                return 1
            
            if n in hmap:
                return hmap[n]
            #n definies the state 
            #i.e n - stair no which is no of ways to reach that nth stairf
            #here it depends of two poss
            ans = ways(n-1)+ways(n-2)
            hmap[n] = ans
            return ans
        return ways(n)
        