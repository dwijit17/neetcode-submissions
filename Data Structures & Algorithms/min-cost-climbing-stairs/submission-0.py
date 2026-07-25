class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hmap = {}
        def coster(i):
            if i==0 or i==1:
                return 0
            if i in hmap:
                return hmap[i]
            c = min(cost[i-1]+coster(i-1),cost[i-2]+coster(i-2))
            hmap[i] = c
            return hmap[i]
        
        return coster(len(cost))
        

        